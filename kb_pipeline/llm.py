import json
import logging
from typing import Any, Optional

import requests

from .config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL, DEEPSEEK_MODEL, SYSTEM_PROMPT, VALID_DOMAINS

logger = logging.getLogger(__name__)


def validate_llm_output(data: dict[str, Any]) -> list[str]:
    required = ["domain", "subdomain", "concept", "title", "summary", "key_points"]
    errors: list[str] = []
    for field in required:
        if field not in data:
            errors.append(f"missing '{field}'")
    if "domain" in data and data["domain"] not in VALID_DOMAINS:
        errors.append(f"invalid domain '{data['domain']}'")
    if "key_points" in data and not isinstance(data["key_points"], list):
        errors.append("'key_points' must be a list")
    return errors


def classify_summarize(
    text: str,
    meta: dict[str, Any],
    audit_feedback: Optional[str] = None,
) -> Optional[dict[str, Any]]:
    if not DEEPSEEK_API_KEY:
        logger.warning("  [!] DEEPSEEK_API_KEY not set, skipping LLM")
        return None

    prompt = (
        f"Title: {meta.get('title', '')}\n"
        f"Author: {meta.get('author', '')}\n"
        f"URL: {meta.get('link', '')}\n"
        f"Date: {meta.get('published', '')}\n\n"
        f"---\n\n{text[:15000]}"
    )
    if audit_feedback:
        prompt += f"\n\n---\nPrevious audit feedback — please address these issues:\n{audit_feedback}"
    try:
        r = requests.post(
            f"{DEEPSEEK_API_URL}/chat/completions",
            headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
            json={
                "model": DEEPSEEK_MODEL,
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
        data = json.loads(content)
        errors = validate_llm_output(data)
        if errors:
            logger.warning("  [!] LLM output validation failed: %s", "; ".join(errors))
            return None
        return data
    except requests.RequestException as e:
        logger.warning("  [!] LLM request failed: %s", e)
    except (json.JSONDecodeError, KeyError, IndexError, TypeError) as e:
        logger.warning("  [!] LLM response parse failed: %s", e)
    return None
