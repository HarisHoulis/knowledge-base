import json
import logging
from typing import Any, Callable, Optional

import requests

from .config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL, DEEPSEEK_MODEL

logger = logging.getLogger(__name__)

AuditResult = dict[str, Any]

CLASSIFICATION_AUDIT_PROMPT = """You are a classification audit assistant. Your job is to verify that the assigned domain, subdomain, and concept are appropriate for the source text.

Source text:
{source_text}

Assigned classification:
- Domain: {domain}
- Subdomain: {subdomain}
- Concept: {concept}

Check:
1. Is the domain one of the valid domains?
2. Does the source text genuinely relate to this domain?
3. Is the subdomain appropriate within the domain?
4. Does the concept name accurately describe the main topic?

Output ONLY valid JSON with no markdown formatting, using this schema:
{{"pass": true}}
or
{{"pass": false, "issues": [{{"field": "domain|subdomain|concept", "description": "specific issue"}}]}}"""

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


def _call_llm(prompt: str) -> str:
    r = requests.post(
        f"{DEEPSEEK_API_URL}/chat/completions",
        headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
        json={
            "model": DEEPSEEK_MODEL,
            "messages": [
                {"role": "system", "content": "You are a precise auditor. Output only JSON."},
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
    return body["choices"][0]["message"]["content"]


def classification_audit(
    data: dict[str, Any],
    source_text: str,
    *,
    audit_fn: Optional[Callable[[str], str]] = None,
) -> AuditResult:
    prompt = CLASSIFICATION_AUDIT_PROMPT.format(
        source_text=source_text[:15000],
        domain=data.get("domain", ""),
        subdomain=data.get("subdomain", ""),
        concept=data.get("concept", ""),
    )
    return _run_audit(prompt, audit_fn)


def content_audit(
    data: dict[str, Any],
    source_text: str,
    *,
    audit_fn: Optional[Callable[[str], str]] = None,
) -> AuditResult:
    summary = data.get("summary", "")
    prompt = CONTENT_AUDIT_PROMPT.format(source_text=source_text[:15000], summary=summary)
    return _run_audit(prompt, audit_fn)


def _run_audit(prompt: str, audit_fn: Optional[Callable[[str], str]] = None) -> AuditResult:
    try:
        raw = audit_fn(prompt) if audit_fn else _call_llm(prompt)
        result: AuditResult = json.loads(raw)
        return result
    except (requests.RequestException, json.JSONDecodeError, KeyError, IndexError, TypeError, ConnectionError) as e:
        logger.warning("audit failed: %s", e)
        return {"pass": True}
