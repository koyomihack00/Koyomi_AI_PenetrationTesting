#!/usr/bin/env python3
from pathlib import Path
import json
import sys
from datetime import datetime, timezone

HIGH_RISK_WORDS = [
    "critical",
    "high",
    "rce",
    "authentication bypass",
    "auth bypass",
    "account takeover",
    "sensitive data",
    "credential exposure",
    "unauthorized access",
    "privilege escalation",
    "saml",
    "ssrf",
    "sql injection",
    "file upload",
]

RISKY_ACTIONS = [
    "exploit",
    "brute force",
    "password spray",
    "credential testing",
    "default credential",
    "auth bypass",
    "state-changing",
    "delete",
    "modify",
    "upload",
    "dos",
    "stress",
]

SAFE_ACTIONS = [
    "recon",
    "service discovery",
    "fingerprint",
    "http review",
    "https review",
    "tls review",
    "header review",
    "cookie review",
    "version detection",
    "source review",
    "evidence collection",
    "report update",
    "dashboard update",
    "notes update",
]

def read_text(path):
    if path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")
    return ""

def classify(text):
    t = text.lower()

    high_risk = any(w in t for w in HIGH_RISK_WORDS)
    risky_action = any(w in t for w in RISKY_ACTIONS)
    safe_action = any(w in t for w in SAFE_ACTIONS)

    if risky_action:
        return "ASK_APPROVAL"
    if high_risk:
        return "PAUSE_FOR_HIGH_IMPACT_REVIEW"
    if safe_action:
        return "AUTO_CONTINUE"
    return "AUTO_CONTINUE"

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

    sources = [
        target / "findings" / "findings.md",
        target / "reports" / "pentest-report-final.md",
        target / "notes" / "status.md",
    ]

    combined = "\n".join(read_text(p) for p in sources)
    decision = classify(combined)

    dashboard = target / "dashboard" / "status.json"
    dashboard.parent.mkdir(parents=True, exist_ok=True)

    data = {}
    if dashboard.exists():
        try:
            data = json.loads(dashboard.read_text(encoding="utf-8"))
        except Exception:
            data = {}

    data["ko_decision"] = decision
    data["ko_decision_updated"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    if decision == "AUTO_CONTINUE":
        data["next_actions"] = ["Continue safe assessment automatically"]
    elif decision == "PAUSE_FOR_HIGH_IMPACT_REVIEW":
        data["next_actions"] = ["Pause and ask user for next step due to high-impact finding"]
    else:
        data["next_actions"] = ["Ask user approval before risky action"]

    dashboard.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"[+] Ko decision: {decision}")

if __name__ == "__main__":
    main()
