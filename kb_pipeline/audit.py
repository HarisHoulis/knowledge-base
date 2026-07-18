from typing import Any

AuditResult = dict[str, Any]


def classification_audit(data: dict[str, Any], source_text: str) -> AuditResult:
    return {"pass": True}


def content_audit(data: dict[str, Any], source_text: str) -> AuditResult:
    return {"pass": True}
