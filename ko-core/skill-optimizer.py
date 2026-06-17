#!/usr/bin/env python3
from pathlib import Path
import json
import sys
from datetime import datetime, timezone

MAX_SKILLS = 3

KEYWORDS = {
    "web-pentest": ["web", "http", "https", "portal", "cms", "moodle", "login", "cookie", "header"],
    "tls-review": ["tls", "ssl", "certificate", "cipher", "https"],
    "recon-osint": ["osint", "domain", "subdomain", "hostname", "whois", "dns"],
    "auth-session-review": ["auth", "login", "session", "cookie", "sso", "saml", "oauth"],
    "cloud-security": ["aws", "azure", "gcp", "cloud", "bucket", "metadata"],
    "mobile-pentest": ["android", "ios", "apk", "ipa", "mobile"],
}

def read_text(path):
    if path.exists():
        return path.read_text(encoding="utf-8", errors="ignore").lower()
    return ""

def score_skills(text):
    scores = {}
    for skill, keys in KEYWORDS.items():
        score = sum(text.count(k) for k in keys)
        if score > 0:
            scores[skill] = score
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

    context_files = [
        target / "CLAUDE.md",
        target / "notes" / "status.md",
        target / "dashboard" / "status.json",
        target / "reports" / "pentest-report-final.md",
    ]

    text = "\n".join(read_text(p) for p in context_files)
    ranked = score_skills(text)

    selected = [x[0] for x in ranked[:MAX_SKILLS]]
    if not selected:
        selected = ["recon-osint"]

    optimized_context = {
        "selected_skills": selected,
        "selection_reason": "Selected top relevant skills only to reduce token usage and avoid loading all skill sources.",
        "max_skills_loaded": MAX_SKILLS,
        "token_strategy": [
            "Read KO_SKILL_INDEX first",
            "Load only selected skill summaries",
            "Avoid reading full upstream repositories unless needed",
            "Prefer existing evidence before new scans",
            "Summarize long outputs before sending back to Claude"
        ],
        "updated": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    }

    out = target / "tmp" / "ko-selected-skills.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(optimized_context, indent=2), encoding="utf-8")

    dashboard = target / "dashboard" / "status.json"
    data = {}
    if dashboard.exists():
        try:
            data = json.loads(dashboard.read_text(encoding="utf-8"))
        except Exception:
            data = {}

    data["selected_skills"] = selected
    data["skill_optimization"] = optimized_context
    dashboard.parent.mkdir(parents=True, exist_ok=True)
    dashboard.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("[+] selected optimized skills:")
    for s in selected:
        print(f" - {s}")

if __name__ == "__main__":
    main()
