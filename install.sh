#!/usr/bin/env bash
set -euo pipefail

CLIENT="${1:-CLIENT_NAME}"
ROOT="$HOME/Desktop/AI_By_Ko"
PROJECT="$ROOT/Work/$CLIENT"
TEMPLATE_DIR="$(cd "$(dirname "$0")" && pwd)"

mkdir -p "$ROOT/Shared" "$ROOT/Work" "$ROOT/CTF" "$ROOT/Mobile" "$ROOT/BugBounty"
mkdir -p "$PROJECT"/{scope,reports/final,scripts,targets,dashboard,notes,tmp}

cp -r "$TEMPLATE_DIR/Shared"/* "$ROOT/Shared/" 2>/dev/null || true
cp "$TEMPLATE_DIR/templates/client/CLAUDE.md" "$PROJECT/CLAUDE.md"
cp "$TEMPLATE_DIR/templates/client/LOCAL_SKILLS_INDEX.md" "$PROJECT/LOCAL_SKILLS_INDEX.md"
cp "$TEMPLATE_DIR/templates/client/scope/targets.txt" "$PROJECT/scope/targets.txt"
cp "$TEMPLATE_DIR/templates/client/scope/domains.txt" "$PROJECT/scope/domains.txt"
cp "$TEMPLATE_DIR/templates/client/scope/roe.md" "$PROJECT/scope/roe.md"
cp "$TEMPLATE_DIR/templates/client/scope/out-of-scope.txt" "$PROJECT/scope/out-of-scope.txt"
cp "$TEMPLATE_DIR/scripts/create-target.sh" "$PROJECT/scripts/create-target.sh"
chmod +x "$PROJECT/scripts/create-target.sh"

cat > "$PROJECT/README.md" <<EOF2
# $CLIENT Ko AI Pentest Workspace

Create a target:

\`\`\`bash
./scripts/create-target.sh <TARGET_IP_OR_HOST>
\`\`\`

Run Claude:

\`\`\`bash
cd targets/<TARGET>
claude "\$(cat ~/Desktop/AI_By_Ko/Shared/prompts/resume-target.md)"
\`\`\`
EOF2

echo "[+] Installed Ko AI Pentest workspace: $PROJECT"
