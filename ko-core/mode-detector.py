#!/usr/bin/env python3

import json
import sys
from pathlib import Path

target = Path(sys.argv[1])

dashboard = target / "dashboard" / "status.json"

mode = "work"

name = str(target).lower()

if "ctf" in name:
    mode = "ctf"
elif "bugbounty" in name:
    mode = "bugbounty"
elif "lab" in name:
    mode = "lab"
elif "web" in name:
    mode = "web"

data = {}

if dashboard.exists():
    try:
        data = json.loads(dashboard.read_text())
    except:
        pass

data["ko_mode"] = mode

dashboard.write_text(
    json.dumps(data, indent=2)
)

print(f"[+] Mode: {mode}")
