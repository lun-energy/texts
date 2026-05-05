#!/usr/bin/env python3
"""
Window Summary Generator

Iterates through energy certificate XML files, extracts window entries,
uses an LLM to generate consolidated summaries, and saves the results.
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Optional
import json
import re
from collections import defaultdict
from html import escape as html_escape
import os

# For LLM API - uncomment the one you want to use
# import openai  # pip install openai
# import anthropic  # pip install anthropic


class WindowEntry:
    """Represents a single window/door entry from XML"""
    
    def __init__(self, status_element, ns):
        self.ns = ns
        self.status_id = status_element.get('ID')
        self.short_text = self._get_text(status_element, 'ShortText')
        self.long_text = self._get_text(status_element, 'LongText')
        self.bi_classification = self._get_text(status_element, 'BIClassification')
        
        # Extract window details
        window_elem = status_element.find('.//bu:Window', ns)
        if window_elem is not None:
            self.area = self._get_text(window_elem, 'Area', 'bu')
            self.u_value = self._get_text(window_elem, 'UValue', 'bu')
            self.num_windows = self._get_text(window_elem, 'NumberOfWindows', 'bu')
            self.orientation = self._get_text(window_elem, 'Orientation', 'bu')
            self.inclination = self._get_text(window_elem, 'Inclination', 'bu')
        else:
            self.area = self.u_value = self.num_windows = None
            self.orientation = self.inclination = None
        
        # Placement context from JSON (filled in later)
        self.placement = None  # dict with story, room, wall info
    
    def _get_text(self, element, tag, prefix='inp'):
        """Safely extract text from XML element"""
        if prefix:
            path = f'{prefix}:{tag}'
        else:
            path = tag
        
        elem = element.find(path, self.ns)
        return elem.text if elem is not None and elem.text else ''
    
    def to_dict(self):
        """Convert to dictionary for easy serialization"""
        return {
            'status_id': self.status_id,
            'short_text': self.short_text,
            'long_text': self.long_text,
            'bi_classification': self.bi_classification,
            'area': self.area,
            'u_value': self.u_value,
            'num_windows': self.num_windows,
            'orientation': self.orientation,
            'inclination': self.inclination,
            'placement': self.placement
        }
    
    def __repr__(self):
        return f"Window(ID={self.status_id}, BIC={self.bi_classification}, {self.short_text})"


class JsonModelExtractor:
    """Extracts window placement context from internal JSON model.
    
    The JSON's window segment IDs match the XML's NON-final Status IDs (GUIDs),
    but the final.xml uses simple numeric IDs. We therefore match by physical
    attributes (area, orientation, inclination).
    """
    
    # Mappings for translating English JSON values to user-facing Danish
    STORY_TYPE_DA = {
        'ground': 'stueetage',
        'first': '1. sal',
        'second': '2. sal',
        'basement': 'kælder',
        'attic': 'tagetage',
    }
    
    ROOM_TYPE_DA = {
        'kitchen': 'køkken',
        'livingRoom': 'stue',
        'bathroom': 'badeværelse',
        'bedroom': 'soveværelse',
        'hallway': 'gang',
        'office': 'kontor',
        'utilityRoom': 'bryggers',
        'diningRoom': 'spisestue',
        'staircase': 'trappe',
        'storage': 'depot',
        # 'custom' rooms typically have a meaningful name; if not, we treat
        # them as a generic "værelse" (Danish for an unlabelled room).
        'custom': 'værelse',
    }
    
    def __init__(self, json_path: Path):
        self.json_path = json_path
        with open(json_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        
        # Index: buildingElementId -> placement context (story, room, wall name)
        # Built by walking walls/ceilings and looking at children references.
        self.placement_by_building_element_id = {}
        
        # List of windows (and doors) found in the JSON, with full attributes
        # Each entry: {area, azimuth, inclination, name, placement, ...}
        self.json_windows = []
        
        self._build_indexes()
    
    def _build_indexes(self):
        """Walk the story/room/wall hierarchy and the windows[] arrays."""
        # The JSON wraps the model under roomByRoomModel.roomByRoomModel.
        # Fall back to home.latestSnapshot, then to the top-level if needed.
        snapshot = (
            self.data.get('roomByRoomModel', {}).get('roomByRoomModel')
            or self.data.get('roomByRoomModel', {}).get('home', {}).get('latestSnapshot')
            or self.data.get('latestSnapshot')
            or self.data
            or {}
        )
        stories = snapshot.get('stories', [])
        
        # Pass 1: Build buildingElementId -> placement map by walking walls/ceilings
        for story in stories:
            story_type = story.get('storyType', '')
            story_da = self.STORY_TYPE_DA.get(story_type, story_type)
            
            for room in story.get('rooms', []):
                room_name = room.get('name', '')
                room_type = room.get('roomType', '')
                room_type_da = self.ROOM_TYPE_DA.get(room_type, room_type)
                
                placement_base = {
                    'story_type': story_type,
                    'story_da': story_da,
                    'room_name': room_name,
                    'room_type': room_type,
                    'room_type_da': room_type_da,
                }
                
                # Walls
                for wall in room.get('walls', []):
                    wall_name = wall.get('name', '')
                    for segment in wall.get('segments', []):
                        for child in segment.get('children', []):
                            be_id = child.get('buildingElementId')
                            if be_id:
                                self.placement_by_building_element_id[be_id] = {
                                    **placement_base,
                                    'wall_name': wall_name,
                                    'element_location': 'wall',
                                }
                
                # Ceilings (skylights)
                for ceiling in room.get('ceilings', []):
                    ceiling_name = ceiling.get('name', '')
                    for segment in ceiling.get('segments', []):
                        for child in segment.get('children', []):
                            be_id = child.get('buildingElementId')
                            if be_id:
                                self.placement_by_building_element_id[be_id] = {
                                    **placement_base,
                                    'wall_name': ceiling_name,
                                    'element_location': 'ceiling',
                                }
        
        # Pass 2: Find each window/door element and attach placement
        for story in stories:
            for room in story.get('rooms', []):
                # Windows are typically stored at room level too, in `windows[]`
                for win in room.get('windows', []):
                    self._extract_window(win, room_level=True, room=room, story=story)
                
                # Walk walls again to find embedded window elements
                for wall in room.get('walls', []):
                    for segment in wall.get('segments', []):
                        for child in segment.get('children', []):
                            if child.get('buildingElementType') in ('window', 'door'):
                                pass  # already processed via id-based lookup
        
        # Pass 3: Walk all top-level windows/doors arrays (snapshot-level)
        # The JSON also has windows defined at higher levels - find the most
        # complete set by walking the entire structure
        self._collect_all_window_elements(snapshot)
        
        # De-duplicate windows by element_id (keep first segment)
        seen = set()
        deduped = []
        for jw in self.json_windows:
            key = (jw.get('element_id'), jw.get('segment_id'))
            if key not in seen:
                seen.add(key)
                deduped.append(jw)
        self.json_windows = deduped
    
    def _collect_all_window_elements(self, obj, parent_path=''):
        """Recursively find all dicts that look like window/door elements with segments."""
        if isinstance(obj, dict):
            # A window/door element has buildingElementType + segments with area/azimuth
            if (obj.get('buildingElementType') in ('window', 'door') 
                    and 'segments' in obj 
                    and isinstance(obj.get('segments'), list)
                    and obj.get('id')):
                
                element_id = obj.get('id')
                element_name = obj.get('name', '')
                element_type = obj.get('buildingElementType')
                
                placement = self.placement_by_building_element_id.get(element_id, {})
                
                for segment in obj['segments']:
                    if 'grossCalculatedArea' in segment or 'azimuth' in segment:
                        self.json_windows.append({
                            'element_id': element_id,
                            'element_name': element_name,
                            'element_type': element_type,
                            'segment_id': segment.get('id'),
                            'area': segment.get('grossCalculatedArea'),
                            'azimuth': segment.get('azimuth'),
                            'inclination': segment.get('inclination'),
                            'placement': placement,
                        })
            
            for key, value in obj.items():
                self._collect_all_window_elements(value, f"{parent_path}.{key}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                self._collect_all_window_elements(item, f"{parent_path}[{i}]")
    
    def _extract_window(self, win, room_level, room, story):
        """Helper for room-level windows (kept for completeness, not actively used)"""
        pass
    
    def find_match(self, area, orientation, inclination,
                   used_keys: set = None,
                   area_tolerance: float = 0.2) -> Optional[dict]:
        """Find the closest JSON window matching given XML attributes.
        
        Matching uses orientation + inclination as hard filters, then picks
        the JSON window whose area is closest to the XML area.
        """
        if used_keys is None:
            used_keys = set()
        if area is None:
            return None
        
        try:
            xml_area = float(area)
            xml_orientation = float(orientation) if orientation else None
            xml_inclination = float(inclination) if inclination else None
        except (ValueError, TypeError):
            return None
        
        candidates = []
        for jw in self.json_windows:
            key = (jw.get('element_id'), jw.get('segment_id'))
            if key in used_keys:
                continue
            if jw['area'] is None:
                continue
            
            az_match = True
            if xml_orientation is not None and jw['azimuth'] is not None:
                az_diff = abs(jw['azimuth'] - xml_orientation)
                az_match = az_diff <= 10 or az_diff >= 350
            
            inc_match = True
            if xml_inclination is not None and jw['inclination'] is not None:
                inc_match = abs(jw['inclination'] - xml_inclination) <= 10
            
            if not (az_match and inc_match):
                continue
            
            area_diff = abs(jw['area'] - xml_area)
            if area_diff <= area_tolerance:
                candidates.append((area_diff, jw))
        
        if not candidates:
            return None
        
        candidates.sort(key=lambda x: x[0])
        return candidates[0][1]
    
    def enrich_windows(self, windows: List[WindowEntry]) -> int:
        """Match XML windows with JSON windows and attach placement info.
        
        Each JSON window is consumed by at most one XML window to avoid
        many XML windows mapping to the same room.
        """
        used_keys = set()
        enriched = 0
        for window in windows:
            match = self.find_match(
                window.area, window.orientation, window.inclination,
                used_keys=used_keys,
            )
            if match:
                used_keys.add((match.get('element_id'), match.get('segment_id')))
                placement = match['placement'].copy() if match['placement'] else {}
                placement['element_name'] = match.get('element_name')
                window.placement = placement
                enriched += 1
        return enriched


class ProjectWindowExtractor:
    """Extracts window entries from XML energy certificate files"""
    
    def __init__(self, xml_path: Path):
        self.xml_path = xml_path
        # Normalize project name: strip ' final' or ' plans' suffix variants
        stem = xml_path.stem
        for suffix in (' final', ' plans'):
            if stem.endswith(suffix):
                stem = stem[: -len(suffix)]
                break
        self.project_name = stem
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()
        
        # Define namespaces
        self.ns = {
            '': 'http://www.ens.dk/EnergyLabel',
            'inp': 'http://www.ens.dk/InputData',
            'bu': 'http://www.ens.dk/BuildingUnits',
            'g': 'http://www.ens.dk/Globals',
            'pdf': 'http://www.ens.dk/PDFReportData'
        }
    
    def extract_windows(self) -> List[WindowEntry]:
        """Extract all window entries from the XML"""
        windows = []
        
        # Find all Status elements that contain Window elements
        statuses = self.root.findall('.//inp:Status', self.ns)
        
        for status in statuses:
            # Check if this status has a Window BuildingUnit
            window_elem = status.find('.//bu:Window', self.ns)
            if window_elem is not None:
                windows.append(WindowEntry(status, self.ns))
        
        return windows
    
    def group_by_classification(self, windows: List[WindowEntry]) -> Dict[str, List[WindowEntry]]:
        """Group windows by BIClassification"""
        grouped = defaultdict(list)
        for window in windows:
            grouped[window.bi_classification].append(window)
        return dict(grouped)
    
    def extract_pdf_window_summaries(self) -> Dict[str, str]:
        """Extract window summaries from PDFReportData section"""
        summaries = {}
        
        # Find PDFReportData BuildingReview Text elements
        pdf_texts = self.root.findall('.//pdf:BuildingReview/pdf:Text', self.ns)
        
        for text_elem in pdf_texts:
            bi_class = text_elem.find('pdf:BIClassification', self.ns)
            status_text = text_elem.find('pdf:StatusText', self.ns)
            
            if bi_class is not None and status_text is not None:
                classification = bi_class.text if bi_class.text else ''
                text_content = status_text.text if status_text.text else ''
                
                # Only include window-related classifications (1-3-x-x)
                if classification.startswith('1-3-'):
                    summaries[classification] = text_content.strip()
        
        return summaries


_GENERIC_ROOM_RE = re.compile(r'^rum\s*\d*$', re.IGNORECASE)


def is_generic_room_name(name: Optional[str]) -> bool:
    """Return True if the room name carries no useful info (e.g. 'Rum', 'Rum 4').
    
    These names come straight from the JSON model when the consultant didn't
    label the room - using them in summaries adds noise rather than meaning.
    """
    if not name:
        return True
    return bool(_GENERIC_ROOM_RE.match(name.strip()))


def orientation_to_compass_da(orientation) -> Optional[str]:
    """Convert a degree azimuth (0-360, 0=N) to a Danish compass direction.
    Returns None if orientation is missing or not parseable.
    """
    if orientation is None or orientation == '':
        return None
    try:
        deg = float(orientation) % 360
    except (ValueError, TypeError):
        return None
    
    # 8-point compass with 45° sectors centered on each direction
    sectors = [
        (22.5, 'nord'),
        (67.5, 'nordøst'),
        (112.5, 'øst'),
        (157.5, 'sydøst'),
        (202.5, 'syd'),
        (247.5, 'sydvest'),
        (292.5, 'vest'),
        (337.5, 'nordvest'),
    ]
    for upper, name in sectors:
        if deg < upper:
            return name
    return 'nord'


class WindowSummarizer:
    """Uses LLM to generate window summaries"""
    
    PROMPT_TEMPLATE = """You are an energy consultant writing user-facing summaries for a Danish energy certificate (energimærke) PDF.

TASK: Create a consolidated Danish summary text for the windows/doors below, all sharing BIClassification {bi_classification}.

CLASSIFICATION GUIDE:
- 1-3-1-0 = Standard windows ("Vinduer")
- 1-3-2-0 = Skylights ("Ovenlysvindue")
- 1-3-3-0 = Doors with glass ("Terrassedør/Yderdør")

WRITING STYLE:
- Danish language
- 1-3 sentences
- Describe glass type accurately (tolags/trelags energirude/termorude/etlags glas)
- Identify the MAJORITY type and describe it first ("Vinduerne er hovedsageligt..." / "primært...")
- HARD RULE: Only mention placement (room, compass, story) when it differentiates one subset of windows from another subset with a DIFFERENT glass type / U-value / construction.
    * If ALL windows in the group are of the same type, write a single short sentence and DO NOT mention any placement at all.
      Example: "Yderdørene er monteret med tolags energirude." (NOT "...placeret i entreen, dagligstuen og soveværelset")
- For windows that DIFFER from the majority, you MUST locate the differing subset using ONE OR MORE of:
    * The exact "rum:" value from the data (e.g. "rum: Bryggers" -> "i bryggerset")
    * The exact "rumtype:" value from the data (e.g. "rumtype: kontor" -> "i et kontor")
    * The "Verdenshjørne:" compass direction (e.g. "mod nordvest")
    * Any room name that explicitly appears in the "Beskrivelse:" free-text from the consultant
- HARD CONSTRAINT: never use a room name or room type that is NOT present in the data above.
  If the data only contains compass directions, you may ONLY use compass directions.
  If a window has no placement info at all, do not attribute it to any room.
- Pick the MINIMUM identifier needed to disambiguate. If room alone is unique, do not also add compass.
- NEVER reproduce literal placeholder strings like "rum 4" or "rum 5" - they are filtered out of the data; rely on rumtype/compass instead.
- Do NOT list every individual window
- Do NOT mention numerical measurements, U-values, degree numbers, or counts
- Do NOT include Danish building-regulation codes such as "BR15", "BR18", "BR23", "HB2023", "energiklasse A/B/C", or "efter BR..." even if they appear in the input data. They are internal classification labels and not relevant for the homeowner reading the PDF.
- 1-3-2-0 (skylights) typically don't need locations - they're all on the roof.

ACCURACY RULES (very important):
- For windows (1-3-1-0) and skylights (1-3-2-0), the umbrella plurals "Vinduerne" and
  "Ovenlysvinduerne" are appropriate for the opening sentence regardless of sub-type
  ("Flerfagsvindue", "Enkeltfagsvindue", etc.).
- For doors (1-3-3-0), DO NOT use a single umbrella plural that lumps different door types
  together. The door types in the data are DISTINCT and must be kept distinct:
    * "Yderdør" -> "yderdøren / yderdørene"
    * "Terrassedør" -> "terrassedøren / terrassedørene"
    * "Skydedørsparti" -> "skydedørspartiet / skydedørspartierne"
  Treat them as separate categories. NEVER write "Yderdørene er ..." about a group that
  contains terrassedøre or skydedørspartier - that conflates the types.
  If the group contains a mix of door types (e.g. 2 skydedørspartier + 1 yderdør), do NOT
  open with a single umbrella plural at all. Instead describe each type separately or group
  by glass type while naming each door's specific type.
- When you need to pick out a specific differing entry, use a TYPE WORD that maps to one of:
  "vinduet/vinduerne", "ovenlysvinduet/-erne", "yderdøren/-ene", "terrassedøren/-ene",
  "skydedørspartiet/-erne", "glasbyggesten" - chosen to match the entry's "Type:" field.
- DO NOT invent door categories that are not in the data. In particular:
    * Never write "hoveddør" if the data only says "Yderdør" (use "yderdøren" instead).
    * Never write "bryggersdør" or "entredør" if the data only says "Yderdør".
    * Never call a "Skydedørsparti" a "Yderdør" or "Terrassedør" - they are distinct.
- COUNT ACCURACY: the number of items you mention must equal the number of entries in the data.
  If the group has 2 entries and they differ, write "den ene ... den anden ..." or
  "Terrassedøren er ... mens yderdøren ...". If all 2 are identical AND of the same door type,
  use the plural ("Yderdørene er ..."). NEVER imply more entries than exist (e.g.
  "Terrassedør og hoveddør ..." when the data has only 1 terrassedør and 1 yderdør would
  falsely suggest 3 doors).

GROUPING RULE (very important):
- Determine the majority by GLASS TYPE / U-VALUE, not by door type. Then group the description
  around glass type, not around door type:
    * Group all entries that share the same glass spec (e.g. all "tolags energirude") together,
      regardless of whether they are terrassedør, yderdør, or skydedørsparti.
    * Then mention the differing entries with their specific door type and location.
- Words like "hovedsageligt" or "primært" describe the WHOLE group across all door types.
  They are only valid if more than half of the entries share that spec.
- Avoid sentences like "Terrassedørene er hovedsageligt monteret med ..." when the
  terrassedøre are actually split 50/50 by glass type. Either drop "hovedsageligt" or
  restructure to group by glass type instead.
- For a 50/50 split between two door types, list both explicitly:
  "Døren i X og døren i Y er ..., mens døren i Z er ..."

EXAMPLES OF GOOD OUTPUT:
- All same type, no placement needed:
  "Vinduerne er monteret med tolags energirude."
  "Ovenlysvinduerne er monteret med trelags energirude."
  "Yderdørene er monteret med tolags termorude."
- Mixed types, locate the minority:
  "Vinduerne er hovedsageligt monteret med tolags termorude. Vinduer i bryggerset er monteret med etlags glas, og vinduer i værelset mod nordvest er monteret med etlags glasrude og forsatsrude."
  "Vinduerne er primært monteret med tolags energirude, dog er enkelte vinduer i kælderen fortsat med etlags glas."
- Two doors, one of each type (matches the data 1:1):
  "Terrassedøren er monteret med tolags energirude, mens yderdøren i entreen har trelags energirude."
  "Yderdøren i bryggerset er uden glas og isoleret, mens skydedørspartiet i stuen er monteret med trelags energirude."
- Three doors, grouped by GLASS TYPE (the right way to handle mixed door types + materials):
  Data:
    1. Terrassedør i dagligstuen - 2 lags energirude
    2. Yderdør i entreen - 2 lags energirude
    3. Terrassedør på 1. sal - 2 lags termorude
  Correct: "Terrassedøren i dagligstuen og yderdøren i entreen er monteret med tolags energirude, mens terrassedøren på 1. sal har tolags termorude."
- Mixed Skydedørsparti + Yderdør (DO NOT lump them under "Yderdørene"):
  Data:
    1. Skydedørsparti i bryggerset - 2 lags termorude
    2. Yderdør i entreen - 2 lags energirude
    3. Skydedørsparti i dagligstuen - 2 lags termorude
  Correct: "Skydedørspartierne er monteret med tolags termorude, mens yderdøren i entreen har tolags energirude."

EXAMPLES OF BAD OUTPUT (do NOT do this):
- "Yderdørene er monteret med tolags energirude, med døre placeret i entreen, dagligstuen og soveværelset." (location is irrelevant - all same type)
- "Yderdørene er monteret med tolags termorude, med en dør i entreen mod vest og en i bryggerset mod nord." (same problem)
- "Ovenlysvinduerne er monteret med trelags energirude, efter BR15." (don't mention BR15 / building regulations)
- "Yderdøren er udført som trelags energirude i energiklasse B." (don't mention energy class labels)
- "Terrassedør og hoveddør med sideparti er monteret med tolags energirude, mens yderdøren har trelags energirude." (only 2 doors in the data: 1 terrassedør + 1 yderdør - this falsely implies 3 doors and invents "hoveddør")
- "Terrassedørene er hovedsageligt monteret med tolags energirude, mens terrassedøren på 1. sal har tolags termorude. Yderdøren har tolags energirude." (when there are only 2 terrassedøre, "hovedsageligt" is wrong - it's a 50/50 split. Group by glass type instead.)
- "Yderdørene er primært monteret med tolags termorude, dog har yderdøren i entreen tolags energirude." (the data is actually 2 skydedørspartier + 1 yderdør - calling all three "yderdørene" conflates skydedørsparti with yderdør. They are distinct types and must be named separately.)

WINDOW/DOOR ENTRIES (BIClassification {bi_classification}):

{window_details}

Generate the consolidated Danish summary text now:"""
    
    def __init__(self, api_key: Optional[str] = None, provider: str = "openai"):
        """
        Initialize summarizer with LLM API
        
        Args:
            api_key: API key for the LLM provider
            provider: "openai" or "anthropic" or "mock" (for testing without API)
        """
        self.provider = provider
        self.api_key = api_key or os.getenv('OPENAI_API_KEY') or os.getenv('ANTHROPIC_API_KEY')
        
        if provider == "openai" and self.api_key:
            import openai
            self.client = openai.OpenAI(api_key=self.api_key)
        elif provider == "anthropic" and self.api_key:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
        elif provider == "mock":
            self.client = None  # Mock mode for testing
        else:
            print("Warning: No API key provided. Using mock mode.")
            self.provider = "mock"
            self.client = None
    
    def summarize_group(self, bi_classification: str, windows: List[WindowEntry]) -> str:
        """Generate summary for a group of windows"""
        
        # Prepare window details
        window_details = []
        for i, window in enumerate(windows, 1):
            details = f"{i}. Type: {window.short_text}"
            if window.long_text:
                details += f"\n   Beskrivelse: {window.long_text}"
            if window.area:
                details += f"\n   Areal: {window.area} m², U-værdi: {window.u_value}"
            if window.num_windows:
                details += f", Antal: {window.num_windows}"
            
            # Compass direction from XML orientation (always available when XML has it)
            compass = orientation_to_compass_da(window.orientation)
            if compass:
                details += f"\n   Verdenshjørne: mod {compass}"
            
            # Add placement context from JSON model (story / room / wall)
            if window.placement:
                p = window.placement
                location_parts = []
                if p.get('story_da'):
                    location_parts.append(f"etage: {p['story_da']}")
                
                room_name = p.get('room_name')
                room_type_da = p.get('room_type_da')
                
                if room_name and not is_generic_room_name(room_name):
                    room_label = room_name
                    if (room_type_da
                            and room_type_da.lower() != room_name.lower()
                            and room_type_da != 'værelse'):
                        room_label = f"{room_name} ({room_type_da})"
                    location_parts.append(f"rum: {room_label}")
                elif room_type_da:
                    # Generic room name (or none); fall back to room type.
                    # 'værelse' (formerly 'rum') is the safe Danish default.
                    location_parts.append(f"rumtype: {room_type_da}")
                
                if p.get('wall_name'):
                    location_parts.append(f"konstruktion: {p['wall_name']}")
                
                if location_parts:
                    details += f"\n   Placering: {', '.join(location_parts)}"
            
            window_details.append(details)
        
        prompt = self.PROMPT_TEMPLATE.format(
            bi_classification=bi_classification,
            window_details="\n\n".join(window_details)
        )
        
        if self.provider == "mock":
            return self._mock_summary(bi_classification, windows)
        elif self.provider == "openai":
            return self._call_openai(prompt)
        elif self.provider == "anthropic":
            return self._call_anthropic(prompt)
    
    def _call_openai(self, prompt: str) -> str:
        """Call OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert in Danish building energy certificates."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=200
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error calling OpenAI: {e}"
    
    def _call_anthropic(self, prompt: str) -> str:
        """Call Anthropic Claude API"""
        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=200,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text.strip()
        except Exception as e:
            return f"Error calling Anthropic: {e}"
    
    def _mock_summary(self, bi_classification: str, windows: List[WindowEntry]) -> str:
        """Generate mock summary for testing without API"""
        classification_map = {
            '1-3-1-0': 'Vinduerne er monteret med tolags energirude.',
            '1-3-2-0': 'Ovenlysvindue er monteret med trelags energirude.',
            '1-3-3-0': 'Terrassedør og hoveddør med sideparti er monteret med energiruder.'
        }
        return classification_map.get(bi_classification, f"[Mock summary for {bi_classification}]")


def find_input_xml(xml_dir: Path, project_name: str) -> Optional[Path]:
    """Find the Plans (input) XML for a project.
    
    Naming convention: most projects use "{project_name}.xml", but a few
    use "{project_name} plans.xml" instead.
    """
    candidates = [
        xml_dir / f"{project_name}.xml",
        xml_dir / f"{project_name} plans.xml",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def main(xml_dir: Optional[Path] = None, output_dir: Optional[Path] = None,
         label: str = ""):
    """Main execution function.
    
    Workflow:
    1. Iterate over `*final.xml` files (consultant-edited output)
    2. For each, find the matching Plans (input) XML and JSON model
    3. Extract windows from the Plans XML (untouched, no consultant text)
    4. Optionally enrich with JSON placement data
    5. Generate LLM summaries from input data only
    6. Pull the PDFReportData summary from the final XML for comparison only
    
    Args:
        xml_dir: Directory containing project XML/JSON files. Defaults to
            repo_root/problem/ (the training set).
        output_dir: Directory where output JSON + markdown reports are written.
            Defaults to the script's own directory.
        label: Optional suffix appended to output filenames. Useful when
            running multiple sets (e.g. label="test_cases" to keep training
            and held-out outputs separate).
    """
    
    # Repo layout: this script lives in experiments/window_summaries/,
    # and the default source data lives at repo_root/problem/.
    repo_root = Path(__file__).resolve().parent.parent.parent
    if xml_dir is None:
        xml_dir = repo_root / "problem"
    if output_dir is None:
        output_dir = Path(__file__).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    suffix = f"_{label}" if label else ""
    output_file = output_dir / f"window_summaries_output{suffix}.json"
    report_file = output_dir / f"window_summaries_report{suffix}.md"
    comparison_file = output_dir / f"window_summaries_comparison{suffix}.md"
    
    print(f"Input dir : {xml_dir}")
    print(f"Output dir: {output_dir}\n")
    
    summarizer = WindowSummarizer(provider="anthropic")
    
    results = {}
    
    final_files = sorted(xml_dir.glob("*final.xml"))
    print(f"Found {len(final_files)} projects to process\n")
    
    for final_file in final_files:
        project_name = final_file.stem.replace(' final', '')
        print(f"Processing: {project_name}")
        
        # Locate the matching Plans (input) XML
        input_xml = find_input_xml(xml_dir, project_name)
        if input_xml is None:
            print(f"  ⚠ No input XML found for {project_name}, skipping.\n")
            continue
        print(f"  Input XML: {input_xml.name}")
        
        # Extract windows from input XML (NOT final - consultant text would leak)
        extractor = ProjectWindowExtractor(input_xml)
        windows = extractor.extract_windows()
        print(f"  Found {len(windows)} window entries in input XML")
        
        if not windows:
            print("  No windows found, skipping.\n")
            continue
        
        # JSON model lookup (uses project_name without 'final')
        json_path = xml_dir / f"{project_name}.json"
        json_used = False
        if json_path.exists():
            try:
                json_extractor = JsonModelExtractor(json_path)
                enriched = json_extractor.enrich_windows(windows)
                print(f"  Enriched {enriched}/{len(windows)} windows with JSON placement data")
                json_used = True
            except Exception as e:
                print(f"  Warning: Could not load JSON model: {e}")
        else:
            print(f"  No JSON model found at {json_path.name}")
        
        grouped = extractor.group_by_classification(windows)
        print(f"  Grouped into {len(grouped)} classifications")
        
        # PDFReportData summaries are pulled from the FINAL XML for comparison only.
        # The final XML is never used as input to the LLM.
        final_extractor = ProjectWindowExtractor(final_file)
        pdf_summaries = final_extractor.extract_pdf_window_summaries()
        if pdf_summaries:
            print(f"  Found {len(pdf_summaries)} existing PDF summaries (from final XML)")
        
        project_results = {
            'project_name': project_name,
            'total_windows': len(windows),
            'groups': {},
            'pdf_summaries': pdf_summaries,
            'json_used': json_used,
            'input_xml': input_xml.name,
            'final_xml': final_file.name,
        }
        
        for bi_class, window_list in grouped.items():
            print(f"    {bi_class}: {len(window_list)} entries", end=" -> ")
            summary = summarizer.summarize_group(bi_class, window_list)
            print(f"'{summary}'")
            
            project_results['groups'][bi_class] = {
                'count': len(window_list),
                'summary': summary,
                'windows': [w.to_dict() for w in window_list]
            }
        
        results[extractor.project_name] = project_results
        print()
    
    # Save results
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Results saved to: {output_file}")
    print(f"✓ Processed {len(results)} projects")
    
    # Generate summary report
    generate_markdown_report(results, report_file)
    
    # Generate focused side-by-side comparison report
    generate_comparison_report(results, comparison_file)


CLASSIFICATION_LABELS = {
    '1-3-1-0': 'Standard windows (Vinduer)',
    '1-3-2-0': 'Skylights (Ovenlysvinduer)',
    '1-3-3-0': 'Doors with glass (Døre/Terrassedøre)',
}


def _normalise_for_comparison(text: str) -> str:
    """Lowercase and collapse whitespace for fuzzy comparison."""
    return re.sub(r'\s+', ' ', text.strip().lower()) if text else ''


def _classify_match(generated: str, pdf: str) -> str:
    """Quick heuristic to label how closely two summaries match.
    
    Returns one of: 'identical', 'equivalent', 'partial', 'differs'.
    """
    g = _normalise_for_comparison(generated)
    p = _normalise_for_comparison(pdf)
    if not g or not p:
        return 'no-pdf'
    if g == p:
        return 'identical'
    
    # Build sets of meaningful Danish keywords
    keyword_pattern = re.compile(
        r'\b(tolags|trelags|etlags|énlags|enkeltlags|energirude|termorude|'
        r'glasrude|forsatsrude|glasbyggesten|kold\s*kant|varm\s*kant|'
        r'isoleret|uisoleret|uden\s*glas|sideparti|ovenlys|'
        r'br15|energiklasse|nord|syd|øst|vest|nordøst|nordvest|'
        r'sydøst|sydvest|køkken|stue|bryggers|værelse|kælder|sal|gang|'
        r'entre|trappe|værksted|garage|terrasse|skydedør|hoveddør|yderdør)\b',
        re.IGNORECASE,
    )
    g_kw = set(keyword_pattern.findall(g))
    p_kw = set(keyword_pattern.findall(p))
    
    if not p_kw:
        return 'partial' if g_kw else 'differs'
    
    overlap = len(g_kw & p_kw) / len(p_kw)
    if overlap >= 0.85:
        return 'equivalent'
    if overlap >= 0.5:
        return 'partial'
    return 'differs'


MATCH_BADGE = {
    'identical': '✅ Identical',
    'equivalent': '✅ Equivalent',
    'partial': '⚠️ Partial overlap',
    'differs': '❌ Differs',
    'no-pdf': '— No PDF text',
}


def generate_comparison_report(results: dict, output_path: Path):
    """Generate a focused side-by-side comparison: Generated vs PDFReportData."""
    
    enriched = [(k, v) for k, v in results.items() if v.get('json_used')]
    plain = [(k, v) for k, v in results.items() if not v.get('json_used')]
    
    lines = [
        "# Generated vs PDFReportData Comparison",
        "",
        "Side-by-side comparison of LLM-generated window/door summaries (from "
        "the Plans input XML) and the consultant's PDFReportData summaries "
        "(from the final XML).",
        "",
        "**Legend:**",
        "- ✅ Identical: byte-equal (after whitespace/case normalisation)",
        "- ✅ Equivalent: ≥85% of the consultant's domain keywords are present in the generated text",
        "- ⚠️ Partial overlap: 50-84% of the consultant's keywords are present",
        "- ❌ Differs: less than 50% keyword overlap",
        "- — No PDF text: consultant did not provide a PDFReportData entry for this classification",
        "",
        "---",
        "",
    ]
    
    # High-level scoreboard
    counts = {k: 0 for k in MATCH_BADGE}
    total_compared = 0
    for _, data in results.items():
        pdfs = data.get('pdf_summaries', {})
        for bi, group in data.get('groups', {}).items():
            label = _classify_match(group['summary'], pdfs.get(bi, ''))
            counts[label] += 1
            if label != 'no-pdf':
                total_compared += 1
    
    lines.extend([
        "## Match Scoreboard",
        "",
        f"Total comparisons (with consultant text): **{total_compared}**",
        "",
        "| Match level | Count |",
        "|---|---|",
    ])
    for label in ['identical', 'equivalent', 'partial', 'differs', 'no-pdf']:
        lines.append(f"| {MATCH_BADGE[label]} | {counts[label]} |")
    lines.extend(['', '---', ''])
    
    def _format_window_entry_html(window: dict) -> str:
        """Format one window entry for the 'Individual Entries' HTML table cell."""
        parts = [f"<strong>{html_escape(window['short_text'])}</strong>"]
        meta = []
        if window.get('area'):
            meta.append(f"{window['area']} m²")
        if window.get('u_value'):
            meta.append(f"U={window['u_value']}")
        if window.get('orientation'):
            compass = orientation_to_compass_da(window['orientation'])
            if compass:
                meta.append(f"mod {compass}")
            else:
                meta.append(f"{window['orientation']}°")
        if meta:
            parts.append(' · '.join(html_escape(m) for m in meta))
        
        placement = window.get('placement') or {}
        loc_parts = []
        if placement.get('story_da'):
            loc_parts.append(placement['story_da'])
        room_name = placement.get('room_name')
        if room_name and not is_generic_room_name(room_name):
            loc_parts.append(room_name)
        elif placement.get('room_type_da'):
            loc_parts.append(placement['room_type_da'])
        if placement.get('wall_name'):
            loc_parts.append(placement['wall_name'])
        if loc_parts:
            parts.append(
                '<em>'
                + html_escape(' / '.join(loc_parts))
                + '</em>'
            )
        return '<br>'.join(parts)
    
    def render_project_table(project_name: str, data: dict):
        """3-column HTML table view for JSON-enriched projects."""
        lines.extend([
            f"## {project_name} (JSON enriched)",
            "",
            f"- Input XML: `{data.get('input_xml', '?')}`",
            f"- Final XML: `{data.get('final_xml', '?')}`",
            "",
        ])
        
        pdfs = data.get('pdf_summaries', {})
        ordered_classes = sorted(
            data.get('groups', {}).keys(),
            key=lambda c: list(CLASSIFICATION_LABELS.keys()).index(c) if c in CLASSIFICATION_LABELS else 99,
        )
        
        # ---- Combined view (all classifications merged) ----
        # Consultants often write a single summary that spans windows + skylights
        # + doors and place it in just one classification's text. The combined
        # view aligns the Generated text and Individual Entries against ALL
        # consultant text for the project.
        all_pdf_parts = []
        for bi_class in ordered_classes:
            txt = pdfs.get(bi_class, '')
            if txt.strip():
                label = CLASSIFICATION_LABELS.get(bi_class, bi_class)
                all_pdf_parts.append(f"[{bi_class}]\n{txt}")
        combined_pdf = '\n\n'.join(all_pdf_parts) if all_pdf_parts else '_(no PDFReportData entries)_'
        
        combined_generated_parts = []
        for bi_class in ordered_classes:
            group = data['groups'][bi_class]
            combined_generated_parts.append(group['summary'].strip())
        # Use blank-line separation so each classification reads as its own paragraph.
        combined_generated = '\n\n'.join(combined_generated_parts)
        
        combined_entries_parts = []
        total_entries = 0
        for bi_class in ordered_classes:
            group = data['groups'][bi_class]
            label = CLASSIFICATION_LABELS.get(bi_class, bi_class)
            heading = f'<strong style="color:#888">— {label} ({group["count"]}) —</strong>'
            combined_entries_parts.append(heading)
            for w in group['windows']:
                combined_entries_parts.append(_format_window_entry_html(w))
            total_entries += group['count']
        
        combined_match = _classify_match(
            combined_generated,
            ' '.join(pdfs.get(c, '') for c in ordered_classes),
        )
        
        combined_pdf_html = '<br><br>'.join(
            html_escape(p) for p in combined_pdf.split('\n\n')
        ).replace('\n', '<br>')
        combined_generated_html = '<br><br>'.join(
            html_escape(p) for p in combined_generated.split('\n\n')
        ).replace('\n', '<br>')
        combined_entries_html = '<br><br>'.join(combined_entries_parts)
        
        lines.extend([
            f"### Combined view (all {total_entries} entries across "
            f"{len(ordered_classes)} classifications) · {MATCH_BADGE[combined_match]}",
            "",
            "<table>",
            "<thead><tr>"
            "<th style=\"width:30%\">PDFReportData (all consultant text)</th>"
            "<th style=\"width:30%\">Generated (all classifications joined)</th>"
            "<th style=\"width:40%\">Individual Entries (all)</th>"
            "</tr></thead>",
            "<tbody><tr>",
            f"<td valign=\"top\">{combined_pdf_html}</td>",
            f"<td valign=\"top\">{combined_generated_html}</td>",
            f"<td valign=\"top\">{combined_entries_html}</td>",
            "</tr></tbody>",
            "</table>",
            "",
            "<details><summary>Per-classification breakdown</summary>",
            "",
        ])
        
        # ---- Per-classification breakdown ----
        for bi_class in ordered_classes:
            group = data['groups'][bi_class]
            label = CLASSIFICATION_LABELS.get(bi_class, bi_class)
            generated = group['summary']
            pdf_text = pdfs.get(bi_class, '') or '_(no PDFReportData entry)_'
            match = _classify_match(generated, pdfs.get(bi_class, ''))
            
            pdf_html = '<br><br>'.join(
                html_escape(p) for p in pdf_text.split('\n\n')
            ).replace('\n', '<br>')
            generated_html = '<br><br>'.join(
                html_escape(p) for p in generated.split('\n\n')
            ).replace('\n', '<br>')
            
            entries_html = '<br><br>'.join(
                _format_window_entry_html(w) for w in group['windows']
            )
            
            lines.extend([
                f"#### {bi_class} — {label} ({group['count']} entries) · "
                f"{MATCH_BADGE[match]}",
                "",
                "<table>",
                "<thead><tr>"
                "<th style=\"width:30%\">PDFReportData (consultant, from Final)</th>"
                "<th style=\"width:30%\">Generated (LLM, from Plans + JSON)</th>"
                "<th style=\"width:40%\">Individual Entries (input)</th>"
                "</tr></thead>",
                "<tbody><tr>",
                f"<td valign=\"top\">{pdf_html}</td>",
                f"<td valign=\"top\">{generated_html}</td>",
                f"<td valign=\"top\">{entries_html}</td>",
                "</tr></tbody>",
                "</table>",
                "",
            ])
        
        lines.extend(["</details>", "", "---", ""])
    
    def render_project(project_name: str, data: dict):
        """Plain 2-column blockquote view for projects without JSON."""
        lines.extend([
            f"## {project_name}",
            "",
            f"- Input XML: `{data.get('input_xml', '?')}`",
            f"- Final XML: `{data.get('final_xml', '?')}`",
            "",
        ])
        
        pdfs = data.get('pdf_summaries', {})
        ordered_classes = sorted(
            data.get('groups', {}).keys(),
            key=lambda c: list(CLASSIFICATION_LABELS.keys()).index(c) if c in CLASSIFICATION_LABELS else 99,
        )
        
        for bi_class in ordered_classes:
            group = data['groups'][bi_class]
            label = CLASSIFICATION_LABELS.get(bi_class, bi_class)
            generated = group['summary']
            pdf_text = pdfs.get(bi_class, '')
            match = _classify_match(generated, pdf_text)
            
            lines.extend([
                f"### {bi_class} — {label} ({group['count']} entries)",
                "",
                f"**Match:** {MATCH_BADGE[match]}",
                "",
                "**Generated (from Plans):**",
                f"> {generated}",
                "",
                "**PDFReportData (from Final, consultant):**",
            ])
            if pdf_text:
                pdf_lines = pdf_text.splitlines()
                for pl in pdf_lines:
                    lines.append(f"> {pl}" if pl.strip() else ">")
            else:
                lines.append("> _(no PDFReportData entry for this classification)_")
            lines.append("")
        
        lines.extend(["---", ""])
    
    if enriched:
        lines.extend(["# Projects with JSON Enrichment", ""])
        for name, data in enriched:
            render_project_table(name, data)
    
    if plain:
        lines.extend(["# Projects without JSON Enrichment", ""])
        for name, data in plain:
            render_project(name, data)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"✓ Comparison report saved to: {output_path}")


def generate_markdown_report(results: dict, output_path: Path):
    """Generate a human-readable markdown report.
    
    Projects that were enriched with JSON model data are listed first,
    followed by projects without JSON enrichment.
    """
    
    enriched_projects = {k: v for k, v in results.items() if v.get('json_used')}
    plain_projects = {k: v for k, v in results.items() if not v.get('json_used')}
    
    lines = [
        "# Window Summary Report",
        "",
        f"Generated summaries for {len(results)} projects "
        f"({len(enriched_projects)} with JSON enrichment, {len(plain_projects)} without)",
        "",
        "---",
        ""
    ]
    
    def render_project(project_name: str, data: dict):
        json_marker = " (JSON enriched)" if data.get('json_used') else ""
        lines.extend([
            f"## {project_name}{json_marker}",
            "",
            f"**Total Windows:** {data['total_windows']}  ",
            f"**Classifications:** {len(data['groups'])}",
            ""
        ])
        
        for bi_class, group_data in data['groups'].items():
            lines.extend([
                f"### {bi_class}",
                "",
                f"**Count:** {group_data['count']} entries  ",
                ""
            ])
            
            pdf_summaries = data.get('pdf_summaries', {})
            if bi_class in pdf_summaries:
                lines.extend([
                    f"**Original PDF Summary:**",
                    f"> {pdf_summaries[bi_class]}",
                    ""
                ])
            
            lines.extend([
                f"**Generated Summary:**",
                f"> {group_data['summary']}",
                "",
                "**Individual Entries:**",
                ""
            ])
            
            for window in group_data['windows']:
                lines.append(f"- {window['short_text']}")
                if window['area']:
                    lines.append(f"  - Area: {window['area']} m², U-value: {window['u_value']}")
                placement = window.get('placement')
                if placement:
                    placement_parts = []
                    if placement.get('story_da'):
                        placement_parts.append(f"Etage: {placement['story_da']}")
                    room_name = placement.get('room_name')
                    if room_name and not is_generic_room_name(room_name):
                        placement_parts.append(f"Rum: {room_name}")
                    elif placement.get('room_type_da'):
                        placement_parts.append(f"Rumtype: {placement['room_type_da']}")
                    if placement.get('wall_name'):
                        placement_parts.append(f"Væg: {placement['wall_name']}")
                    if placement_parts:
                        lines.append(f"  - Placering: {' | '.join(placement_parts)}")
            
            lines.append("")
        
        lines.append("---")
        lines.append("")
    
    if enriched_projects:
        lines.extend([
            "# Projects with JSON Enrichment",
            "",
            "These projects had a matching internal JSON model file, so each window "
            "is annotated with story, room, and wall placement context.",
            "",
            "---",
            "",
        ])
        for name, data in enriched_projects.items():
            render_project(name, data)
    
    if plain_projects:
        lines.extend([
            "# Projects without JSON Enrichment",
            "",
            "These projects only had the energy-certificate XML available; "
            "summaries are based on window attributes alone.",
            "",
            "---",
            "",
        ])
        for name, data in plain_projects.items():
            render_project(name, data)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"✓ Markdown report saved to: {output_path}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Generate Danish window/door summaries with an LLM and "
                    "compare them to the consultant's PDFReportData."
    )
    parser.add_argument(
        '--xml-dir',
        type=Path,
        default=None,
        help="Directory containing project XML + JSON files. Defaults to "
             "repo_root/problem/ (the training set).",
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=None,
        help="Directory where output JSON + markdown reports are written. "
             "Defaults to this script's directory.",
    )
    parser.add_argument(
        '--label',
        type=str,
        default="",
        help="Suffix appended to output filenames (e.g. 'test_cases').",
    )
    args = parser.parse_args()
    
    main(xml_dir=args.xml_dir, output_dir=args.output_dir, label=args.label)
