from kb_pipeline.fetcher import _strip_subtitle_formatting, extract_text


SAMPLE_VTT = """WEBVTT
Kind: captions
Language: en

00:00:00.320 --> 00:00:18.790 align:start position:0%

[Music]

00:00:18.800 --> 00:00:21.790 align:start position:0%
We're<00:00:19.039><c> no</c><00:00:19.359><c> strangers</c><00:00:19.840><c> to</c>

00:00:21.800 --> 00:00:25.950 align:start position:0%
love. You know the rules and so do"""


class TestStripSubtitleFormatting:
    def test_strips_webvtt_header(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert "WEBVTT" not in result
        assert "Kind:" not in result
        assert "Language:" not in result

    def test_strips_timestamps(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert "-->" not in result

    def test_strips_inline_tags(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert "<c>" not in result
        assert "We're no strangers to" in result

    def test_preserves_text_content(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert "We're no strangers to" in result
        assert "love" in result
        assert "You know the rules" in result

    def test_returns_single_string(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT)
        assert isinstance(result, str)
        assert len(result) > 0


SAMPLE_VTT_EMPTY = "WEBVTT\nKind: captions\nLanguage: en\n"

SAMPLE_VTT_NONTEXT = """WEBVTT
Kind: captions
Language: en

00:00:01.000 --> 00:00:02.000 align:start position:0%

1

00:00:02.000 --> 00:00:03.000 align:start position:0%

2"""


class TestStripSubtitleFormattingEdgeCases:
    def test_empty_returns_empty_string(self):
        assert _strip_subtitle_formatting("") == ""

    def test_only_metadata_returns_empty_string(self):
        assert _strip_subtitle_formatting(SAMPLE_VTT_EMPTY) == ""

    def test_only_timestamp_lines_returns_empty_string(self):
        assert _strip_subtitle_formatting("00:00:01.000 --> 00:00:02.000") == ""

    def test_numeric_index_lines_skipped(self):
        result = _strip_subtitle_formatting(SAMPLE_VTT_NONTEXT)
        assert result == ""


SAMPLE_PLAIN_TEXT = """Exploring /grill-me new batch-based question system.
Learn how Matt is improving the skill by asking questions in rounds
instead of one-by-one, reducing wait times and context switching."""


class TestExtractText:
    def test_empty_returns_empty_string(self):
        assert extract_text("") == ""

    def test_whitespace_only_returns_empty_string(self):
        assert extract_text("   \n  \t  ") == ""

    def test_plain_text_returns_unchanged(self):
        result = extract_text(SAMPLE_PLAIN_TEXT)
        assert result == SAMPLE_PLAIN_TEXT

    def test_html_delegates_to_trafilatura(self):
        html = "<html><body><p>Hello world</p></body></html>"
        result = extract_text(html)
        assert isinstance(result, str)
        assert len(result) > 0
