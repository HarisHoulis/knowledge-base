from typing import Any

class FeedParserDict(dict[str, Any]):
    bozo: bool
    entries: list[FeedParserDict]
    bozo_exception: Exception | None

def parse(
    url_file_stream_or_string: str | bytes,
    etag: str | None = None,
    modified: str | None = None,
    agent: str | None = None,
    referrer: str | None = None,
    handlers: list[Any] | None = None,
    request_headers: dict[str, str] | None = None,
    response_headers: dict[str, str] | None = None,
    resolve_relative_uris: bool | None = None,
    sanitize_html: bool | None = None,
) -> FeedParserDict: ...
