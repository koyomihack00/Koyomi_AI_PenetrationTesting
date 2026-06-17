#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-}"
if [ -z "$TARGET" ]; then
  echo "Usage: $0 <target-ip-or-host>"
  exit 1
fi

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ROOT="$HOME/Desktop/AI_By_Ko"
TEMPLATE="$ROOT/Shared/templates/target-template"
DEST="$PROJECT_DIR/targets/$TARGET"

if [ ! -d "$TEMPLATE" ]; then
  echo "[-] Template not found: $TEMPLATE"
  exit 1
fi

mkdir -p "$PROJECT_DIR/targets"
cp -r "$TEMPLATE" "$DEST"

echo "$TARGET" > "$DEST/scope/targets.txt"
find "$DEST" -type f -exec sed -i "s/TARGET_PLACEHOLDER/$TARGET/g" {} +

if ! grep -qxF "$TARGET" "$PROJECT_DIR/scope/targets.txt" 2>/dev/null; then
  echo "$TARGET" >> "$PROJECT_DIR/scope/targets.txt"
  sort -u "$PROJECT_DIR/scope/targets.txt" -o "$PROJECT_DIR/scope/targets.txt"
fi

echo "[+] Created target workspace: $DEST"
