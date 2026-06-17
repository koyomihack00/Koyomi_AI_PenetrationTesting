#!/usr/bin/env python3
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from severity_engine import renumber_findings

def load_findings(target: Path):
    fjson = target / "findings" / "findings.json"
    if fjson.exists():
        return json.loads(fjson.read_text(encoding="utf-8")).get("findings", [])
    return []

def build_final_section(findings):
    findings = renumber_findings(findings)

    lines = []
    lines.append("# Final Sorted Findings")
    lines.append("")
    lines.append("| Final ID | Original ID | Severity | Title |")
    lines.append("|---|---|---|---|")

    for f in findings:
        lines.append(f"| {f.get('final_id')} | {f.get('original_id')} | {f.get('severity')} | {f.get('title')} |")

    lines.append("")
    lines.append("## Detailed Findings")
    lines.append("")

    for f in findings:
        lines.append(f"## {f.get('final_id')} - {f.get('title')}")
        lines.append("")
        lines.append(f"Original ID: {f.get('original_id')}")
        lines.append(f"Severity: {f.get('severity')}")
        lines.append("")
        lines.append("Resolution Status: TBD")
        lines.append("")
        lines.append("Risk Confirmed: TBD")
        lines.append("")
        lines.append("Raw Evidence Summary:")
        lines.append("")
        lines.append(f.get("raw", "Pending."))
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    report = target / "reports" / "pentest-report-final.md"

    findings = load_findings(target)
    section = build_final_section(findings)

    report.parent.mkdir(parents=True, exist_ok=True)

    old = report.read_text(encoding="utf-8", errors="ignore") if report.exists() else ""
    marker = "\n\n---\n\n# Ko Core Generated Final Section\n\n"

    if "# Ko Core Generated Final Section" in old:
        old = old.split("# Ko Core Generated Final Section")[0].rstrip()

    report.write_text(old.rstrip() + marker + section + "\n", encoding="utf-8")
    print(f"[+] updated report -> {report}")

if __name__ == "__main__":
    main()
