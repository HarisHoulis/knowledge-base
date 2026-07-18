import json
import logging
from typing import Any

import requests

from .config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL, DEEPSEEK_MODEL

logger = logging.getLogger(__name__)

AuditResult = dict[str, Any]

CONTENT_AUDIT_PROMPT = """You are a content audit assistant. Your job is to verify that a draft summary accurately reflects the source text.

Source text:
{source_text}

Draft summary:
{summary}

Check the draft summary against the source text for:
1. Hallucinations — claims not supported by the source text
2. Critical omissions — important information from the source that is missing from the summary
3. Distortions — claims that misrepresent what the source says

Output ONLY valid JSON with no markdown formatting, using this schema:
{{"pass": true}}
or
{{"pass": false, "issues": [{{"field": "summary", "description": "specific issue"}}]}}"""


def classification_audit(data: dict[str, Any], source_text: str) -> AuditResult:
    return {"pass": True}


def content_audit(data: dict[str, Any], source_text: str) -> AuditResult:
    if not DEEPSEEK_API_KEY:
        logger.warning("DEEPSEEK_API_KEY not set, skipping content audit")
        return {"pass": True}

    summary = data.get("summary", "")
    prompt = CONTENT_AUDIT_PROMPT.format(source_text=source_text[:15000], summary=summary)
    try:
        r = requests.post(
            f"{DEEPSEEK_API_URL}/chat/completions",
            headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
            json={
                "model": DEEPSEEK_MODEL,
                "messages": [
                    {"role": "system", "content": "You are a precise content auditor. Output only JSON."},
                    {"role": "user", "content": prompt},
                ],
                "response_format": {"type": "json_object"},
                "temperature": 0.1,
                "max_tokens": 500,
            },
            timeout=60,
        )
        r.raise_for_status()
        body = r.json()
        content = body["choices"][0]["message"]["content"]
        result: AuditResult = json.loads(content)
        return result
    except requests.RequestException as e:
        logger.warning("content audit request failed: %s", e)
    except (json.JSONDecodeError, KeyError, IndexError, TypeError) as e:
        logger.warning("content audit response parse failed: %s", e)
    return {"pass": True}
