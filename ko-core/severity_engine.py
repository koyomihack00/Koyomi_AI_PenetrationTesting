#!/usr/bin/env python3

ORDER = {
    "critical": 1,
    "high": 2,
    "medium": 3,
    "low": 4,
    "informational": 5,
    "info": 5,
    "positive": 6,
    "passed": 6
}

def severity_rank(severity: str) -> int:
    return ORDER.get((severity or "").strip().lower(), 99)

def sort_findings(findings):
    return sorted(findings, key=lambda f: severity_rank(f.get("severity", "")))

def renumber_findings(findings):
    sorted_findings = sort_findings(findings)
    for i, finding in enumerate(sorted_findings, 1):
        finding["final_id"] = f"F-{i:03d}"
        finding.setdefault("original_id", finding.get("id", finding["final_id"]))
    return sorted_findings
