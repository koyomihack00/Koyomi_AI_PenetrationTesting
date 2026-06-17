#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path.cwd()

def parse_findings_md(path: Path):
    findings = []
    if not path.exists():
        return findings

    text = path.read_text(encoding="utf-8", errors="ignore")
    chunks = re.split(r"\n(?=##?\s*F-\d+)", text)

    for chunk in chunks:
        fid = re.search(r"(F-\d+)", chunk)
        sev = re.search(r"Severity:\s*([A-Za-z /]+)", chunk)
        title = re.search(r"#+\s*(F-\d+\s*[-–]\s*)?(.*)", chunk)

        if fid:
            findings.append({
                "id": fid.group(1),
                "title": title.group(2).strip() if title else fid.group(1),
                "severity": sev.group(1).strip() if sev else "Informational",
                "raw": chunk.strip()
            })

    return findings

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    findings_file = target / "findings" / "findings.md"
    out_file = target / "findings" / "findings.json"

    findings = parse_findings_md(findings_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps({"findings": findings}, indent=2), encoding="utf-8")

    print(f"[+] parsed {len(findings)} findings -> {out_file}")

if __name__ == "__main__":
    main()
