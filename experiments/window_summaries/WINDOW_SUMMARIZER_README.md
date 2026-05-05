# Window Summarizer Script

Python script to extract window entries from energy certificate XML files and generate consolidated summaries using an LLM.

## Features

- ✅ Parses multiple XML energy certificate files
- ✅ Extracts window/door entries with full specifications
- ✅ Groups windows by BIClassification (1-3-1-0, 1-3-2-0, 1-3-3-0)
- ✅ Uses LLM to generate Danish summaries
- ✅ Supports OpenAI, Anthropic, or mock mode
- ✅ Outputs JSON and Markdown reports

## Installation

```bash
# Install required packages
pip install openai anthropic

# Or just for specific provider:
pip install openai    # For OpenAI GPT-4
pip install anthropic # For Claude
```

## Usage

### 1. Basic Usage (Mock Mode - No API Key Required)

```bash
python summarize_windows.py
```

This runs in mock mode with pre-defined summaries for testing.

### 2. With OpenAI API

```bash
# Set your API key
export OPENAI_API_KEY="sk-..."

# Edit the script to use OpenAI:
# Change line: summarizer = WindowSummarizer(provider="mock")
# To:          summarizer = WindowSummarizer(provider="openai")

python summarize_windows.py
```

### 3. With Anthropic Claude API

```bash
# Set your API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Edit the script to use Anthropic:
# Change line: summarizer = WindowSummarizer(provider="mock")
# To:          summarizer = WindowSummarizer(provider="anthropic")

python summarize_windows.py
```

## Configuration

Edit the script to customize:

```python
# In main() function:

# Change XML directory
xml_dir = Path(__file__).parent / "problem"

# Change output files
output_file = Path(__file__).parent / "window_summaries_output.json"

# Change LLM provider
summarizer = WindowSummarizer(provider="openai")  # or "anthropic" or "mock"

# Change OpenAI model
# In _call_openai() method, change:
model="gpt-4"  # to "gpt-4o", "gpt-3.5-turbo", etc.

# Change Anthropic model
# In _call_anthropic() method, change:
model="claude-3-5-sonnet-20241022"  # to other Claude models
```

## Output Files

### 1. `window_summaries_output.json`
Complete JSON output with:
- All window entries
- Groupings by classification
- Generated summaries
- Full technical specifications

### 2. `window_summaries_report.md`
Human-readable Markdown report with:
- Project summaries
- Window classifications
- Generated summary texts
- Individual window details

## Example Output

```
Processing: Ivarsvej_27_5200_Odense_V final.xml
  Found 10 window entries
  Grouped into 3 classifications
    1-3-1-0: 6 entries -> 'Vinduerne er monteret med tolags energirude.'
    1-3-2-0: 2 entries -> 'Ovenlysvindue er monteret med trelags energirude.'
    1-3-3-0: 2 entries -> 'Terrassedør og hoveddør med sideparti er monteret med energiruder.'

✓ Results saved to: window_summaries_output.json
✓ Markdown report saved to: window_summaries_report.md
✓ Processed 10 projects
```

## Script Structure

```
WindowEntry
├── Represents single window from XML
└── Extracts: ID, ShortText, LongText, BIClassification, Area, U-value, etc.

ProjectWindowExtractor
├── Parses XML files
├── Extracts all window Status elements
└── Groups by BIClassification

WindowSummarizer
├── Manages LLM API calls
├── Generates prompts per classification group
└── Supports multiple providers (OpenAI, Anthropic, Mock)

main()
├── Iterates through XML files
├── Extracts and groups windows
├── Generates summaries
└── Saves JSON and Markdown outputs
```

## Customizing the Prompt

The LLM prompt is defined in `WindowSummarizer.PROMPT_TEMPLATE`. Edit it to:
- Change output language
- Adjust summary style
- Add/remove technical details
- Modify grouping rules

## BIClassification Reference

| Code | Type | Description |
|------|------|-------------|
| 1-3-1-0 | Standard Windows | Regular windows (Flerfagsvinduer) |
| 1-3-2-0 | Skylights | Roof windows (Ovenlysvindue) |
| 1-3-3-0 | Doors with Glass | Doors with side panels (Terrassedør/Yderdør) |

## Troubleshooting

### No windows found
- Check that XML files contain `<Status>` elements with `<Window>` BuildingUnit
- Verify namespace definitions match your XML structure

### API errors
- Verify API key is set correctly
- Check API rate limits
- Try mock mode first to test script logic

### Encoding issues
- Script uses UTF-8 for Danish characters
- Ensure your terminal supports UTF-8

## Cost Considerations

- **OpenAI GPT-4**: ~$0.01-0.03 per project
- **Anthropic Claude**: ~$0.01-0.02 per project
- **Mock mode**: Free (no API calls)

For 10 projects: ~$0.10-0.30 total

## Next Steps

1. Test with mock mode first
2. Try with one project using real LLM
3. Review output quality
4. Adjust prompt if needed
5. Process all projects

## Related Files

- `WINDOW_SUMMARY_PROMPT.md` - Detailed prompt engineering guide
- `WINDOW_COMPARISON_ANALYSIS.md` - Analysis of window transformation pattern
