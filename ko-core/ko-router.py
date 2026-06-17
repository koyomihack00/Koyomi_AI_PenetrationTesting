#!/usr/bin/env python3
from pathlib import Path
import json
import sys

def detect_target_profile(target: Path):
    text = ""

    for file in [
        target / "CLAUDE.md",
        target / "notes" / "status.md",
        target / "dashboard" / "status.json"
    ]:
        if file.exists():
            text += file.read_text(encoding="utf-8", errors="ignore").lower()

    profile = {
        "web": any(x in text for x in ["web", "http", "https", "portal", "cms", "moodle"]),
        "tls": any(x in text for x in ["tls", "ssl", "certificate", "https"]),
        "osint": any(x in text for x in ["osint", "domain", "hostname"]),
        "auth": any(x in text for x in ["login", "authenticated", "session", "credential"]),
        "cloud": any(x in text for x in ["cloud", "s3", "azure", "aws", "gcp"]),
        "mobile": any(x in text for x in ["android", "ios", "mobile", "apk"])
    }

    selected = []
    if profile["web"]:
        selected.append("web-pentest")
    if profile["tls"]:
        selected.append("tls-review")
    if profile["osint"]:
        selected.append("recon-osint")
    if profile["auth"]:
        selected.append("auth-session-review")
    if profile["cloud"]:
        selected.append("cloud-security")
    if profile["mobile"]:
        selected.append("mobile-pentest")

    if not selected:
        selected.append("recon-osint")

    return profile, selected

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    profile, selected = detect_target_profile(target)

    dashboard = target / "dashboard" / "status.json"
    dashboard.parent.mkdir(parents=True, exist_ok=True)

    data = {}
    if dashboard.exists():
        try:
            data = json.loads(dashboard.read_text(encoding="utf-8"))
        except Exception:
            data = {}

    data["selected_skills"] = selected
    data["ko_profile"] = profile
    data["current_phase"] = "ko_core_routing_complete"

    dashboard.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print("[+] selected skills:")
    for s in selected:
        print(f" - {s}")

if __name__ == "__main__":
    main()
