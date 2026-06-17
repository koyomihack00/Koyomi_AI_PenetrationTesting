#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "ko-core"

def run(cmd):
    print(f"[+] {' '.join(map(str, cmd))}")
    subprocess.run(cmd, check=True)

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

    run(["python3", str(CORE / "mode-detector.py"), str(target)])
    run(["python3", str(CORE / "skill-loader.py")])
    run(["python3", str(CORE / "skill-optimizer.py"), str(target)])
    run(["python3", str(CORE / "ko-router.py"), str(target)])
    run(["python3", str(CORE / "decision-engine.py"), str(target)])
    run(["python3", str(CORE / "finding-engine.py"), str(target)])
    run(["python3", str(CORE / "report-engine.py"), str(target)])

    print("[+] Ko Core workflow complete")

if __name__ == "__main__":
    main()
