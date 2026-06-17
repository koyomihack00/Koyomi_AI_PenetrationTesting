#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SKILL_SOURCES = ROOT / "Shared" / "skills" / "sources"
OUT = ROOT / "Shared" / "skills" / "ko-ai-pentest" / "references" / "KO_SKILL_INDEX.json"

def main():
    skills = []
    for path in SKILL_SOURCES.rglob("SKILL.md"):
        skills.append({
            "name": path.parent.name,
            "path": str(path.relative_to(ROOT)),
            "source": path.parts[-3] if len(path.parts) > 3 else "unknown"
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"skills": skills}, indent=2), encoding="utf-8")
    print(f"[+] indexed {len(skills)} skills -> {OUT}")

if __name__ == "__main__":
    main()
