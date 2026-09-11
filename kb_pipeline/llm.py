import json
import logging
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Optional, Union

import requests

from .config import (
    LLM_API_KEY,
    LLM_API_URL,
    LLM_MODEL,
    OUT_OF_SCOPE,
    SYSTEM_PROMPT,
    VALID_DOMAINS,
)

logger = logging.getLogger(__name__)


class ClassifyFailureKind(str, Enum):
    NO_API_KEY = "no_api_key"
    REQUEST = "request"
    PARSE = "parse"
    VALIDATION = "validation"


@dataclass(frozen=True)
class ClassifyFailure:
    kind: ClassifyFailureKind
    detail: str = ""


def validate_llm_output(data: dict[str, Any]) -> list[str]:
    required = ["domain", "subdomain", "concept", "title", "summary", "key_points"]
    errors: list[str] = []
    for field in required:
        if field not in data:
            errors.append(f"missing '{field}'")
    if (
        "domain" in data
        and data["domain"] not in VALID_DOMAINS
        and data["domain"] != OUT_OF_SCOPE
    ):
        errors.append(f"invalid domain '{data['domain']}'")
    if "key_points" in data and not isinstance(data["key_points"], list):
        errors.append("'key_points' must be a list")
    return errors


def classify_summarize(
    text: str,
    meta: dict[str, Any],
    audit_feedback: Optional[str] = None,
    *,
    post_fn: Optional[Callable[..., Any]] = None,
) -> Union[dict[str, Any], ClassifyFailure]:
    if not LLM_API_KEY:
        logger.warning("  [!] LLM_API_KEY not set, skipping LLM")
        return ClassifyFailure(ClassifyFailureKind.NO_API_KEY, "LLM_API_KEY not set")

    body: Any = {}
    content = ""
    prompt = (
        f"Title: {meta.get('title', '')}\n"
        f"Author: {meta.get('author', '')}\n"
        f"URL: {meta.get('link', '')}\n"
        f"Date: {meta.get('published', '')}\n\n"
        f"---\n\n{text[:15000]}"
    )
    if audit_feedback:
        prompt += (
            "\n\n---\nPrevious audit feedback — please address these issues:\n"
            f"{audit_feedback}"
        )
    try:
        call = post_fn or requests.post
        r = call(
            f"{LLM_API_URL}/chat/completions",
            headers={"Authorization": f"Bearer {LLM_API_KEY}"},
            json={
                "model": LLM_MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                "response_format": {"type": "json_object"},
                "temperature": 0.3,
                "max_tokens": 2000,
            },
            timeout=60,
        )
        r.raise_for_status()
        body = r.json()
        content = body["choices"][0]["message"]["content"]
        content = content if isinstance(content, str) else ""
        data = json.loads(content)
        errors = validate_llm_output(data)
        if errors:
            detail = "; ".join(errors)
            logger.warning("  [!] LLM output validation failed: %s", detail)
            return ClassifyFailure(ClassifyFailureKind.VALIDATION, detail)
        return data
    except requests.RequestException as e:
        logger.warning("  [!] LLM request failed: %s", e)
        return ClassifyFailure(ClassifyFailureKind.REQUEST, str(e))
    except json.JSONDecodeError as e:
        c0 = (body.get("choices") or [{}])[0]
        usage = body.get("usage") or {}
        excerpt = (content[:200] + "...") if len(content) > 200 else content
        logger.warning(
            "  [!] LLM response parse failed: %s | title=%r | finish_reason=%r | "
            "len(content)=%d | usage=%s | content_excerpt=%r",
            e,
            meta.get("title", ""),
            c0.get("finish_reason"),
            len(content),
            usage,
            excerpt,
        )
        return ClassifyFailure(ClassifyFailureKind.PARSE, str(e))
    except (KeyError, IndexError, TypeError) as e:
        logger.warning("  [!] LLM response parse failed: %s", e)
        return ClassifyFailure(ClassifyFailureKind.PARSE, str(e))
