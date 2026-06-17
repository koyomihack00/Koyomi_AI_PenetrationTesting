#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-$(pwd)}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

python3 "$ROOT/ko-core/workflow-engine.py" "$TARGET"
