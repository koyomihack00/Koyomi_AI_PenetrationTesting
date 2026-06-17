#!/usr/bin/env python3
from pathlib import Path
import json
import os
import socket
import sys
from datetime import datetime, timezone

def port_open(host="127.0.0.1", port=9876, timeout=1.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

    burp_enabled = False
    reasons = []

    if port_open("127.0.0.1", 9876):
        burp_enabled = True
        reasons.append("127.0.0.1:9876 open")

    checks = [
        Path.home() / ".claude.json",
        Path.home() / ".claude" / "settings.json",
        target / ".mcp.json",
        target / ".claude" / "mcp.json",
    ]

    for p in checks:
        if p.exists():
            txt = p.read_text(encoding="utf-8", errors="ignore").lower()
            if "burp" in txt or "burpsuite" in txt or "127.0.0.1:9876" in txt:
                burp_enabled = True
                reasons.append(str(p))

    if os.environ.get("BURP_MCP_URL"):
        burp_enabled = True
        reasons.append("BURP_MCP_URL environment variable")

    dashboard = target / "dashboard" / "status.json"
    dashboard.parent.mkdir(parents=True, exist_ok=True)

    data = {}
    if dashboard.exists():
        try:
            data = json.loads(dashboard.read_text(encoding="utf-8"))
        except Exception:
            data = {}

    data["burpsuite_mcp"] = {
        "available": burp_enabled,
        "endpoint": "http://127.0.0.1:9876",
        "mode": "sse",
        "detected_from": reasons,
        "updated": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    }

    if burp_enabled:
        skills = data.get("selected_skills", [])
        if "burp-assisted-web-pentest" not in skills:
            skills.append("burp-assisted-web-pentest")
        data["selected_skills"] = skills

    dashboard.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print(f"[+] BurpSuite MCP available: {burp_enabled}")
    print("[+] Endpoint: http://127.0.0.1:9876")
    for r in reasons:
        print(f" - {r}")

if __name__ == "__main__":
    main()
