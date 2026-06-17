# Ko AI Pentest Project Template

Ko AI Pentest is a Claude Code-ready pentest workspace template for authorized security assessments. It gives each client and each target its own isolated folder, scope files, Claude instructions, reporting structure, dashboard JSON, evidence folders, and optional credential handling.

> Use this project only for authorized security testing. Do not test targets you do not own or do not have written permission to assess.

## What This Template Provides

- Client workspace generator
- Per-target workspace generator
- Claude Code instructions through `CLAUDE.md`
- Safe autonomous assessment workflow
- Scope enforcement
- Skills/agents indexing
- Unified Ko AI meta-skill wrapper
- Live report logging to `reports/pentest-report-final.md`
- Dashboard status tracking in `dashboard/status.json`
- Final report sorting by severity, then renumbering final IDs
- Optional shared credential file support with redaction rules
- GitHub-safe `.gitignore` defaults

## Project Layout

```text
AI_By_Ko/
├── Shared/
│   ├── prompts/
│   │   └── resume-target.md
│   ├── skills/
│   │   └── ko-ai-pentest/
│   │       ├── SKILL.md
│   │       ├── references/
│   │       │   └── KO_SKILL_INDEX.md
│   │       └── scripts/
│   │           └── build-ko-skill-index.sh
│   └── templates/
│       └── target-template/
│           ├── CLAUDE.md
│           ├── scope/
│           ├── scans/
│           ├── evidence/
│           ├── findings/
│           ├── notes/
│           ├── dashboard/
│           ├── reports/
│           ├── scripts/
│           ├── tmp/
│           ├── .claude/
│           └── secrets/
└── Work/
    └── CLIENT_NAME/
        ├── CLAUDE.md
        ├── LOCAL_SKILLS_INDEX.md
        ├── scope/
        ├── reports/final/
        ├── scripts/
        └── targets/
```

## Install

```bash
unzip Ko-AI-Pentest-GitHub-Ready.zip -d ~/Desktop/
cd ~/Desktop/Ko-AI-Pentest-GitHub-Ready
chmod +x install.sh
./install.sh CLIENT_NAME
```

Example:

```bash
./install.sh CMA
```

This creates:

```text
~/Desktop/AI_By_Ko/Work/CMA/
```

## Add Targets

```bash
cd ~/Desktop/AI_By_Ko/Work/CMA
./scripts/create-target.sh 1.2.3.4
```

The script creates:

```text
targets/1.2.3.4/
├── CLAUDE.md
├── scope/targets.txt
├── scans/
├── evidence/
├── findings/findings.md
├── notes/status.md
├── dashboard/status.json
├── reports/pentest-report-final.md
└── .claude/settings.local.json
```

## Start Claude Code for a Target

```bash
cd ~/Desktop/AI_By_Ko/Work/CMA/targets/1.2.3.4
claude "$(cat ~/Desktop/AI_By_Ko/Shared/prompts/resume-target.md)"
```

## Scope Model

Master scope lives at:

```text
Work/<CLIENT>/scope/targets.txt
Work/<CLIENT>/scope/domains.txt
Work/<CLIENT>/scope/roe.md
Work/<CLIENT>/scope/out-of-scope.txt
```

Each target also has its own local scope file:

```text
targets/<TARGET>/scope/targets.txt
```

Ko must confirm scope before testing. If a target is not in the master scope, it should stop as scope-blocked.

## Skills Model

This template includes a unified Ko AI meta-skill:

```text
Shared/skills/ko-ai-pentest/SKILL.md
```

It is designed to coordinate local skill sources such as:

- `offensive-claude`
- `9arm-skills`
- `osint-skill`

Recommended setup using git submodules:

```bash
git submodule add https://github.com/hypnguyen1209/offensive-claude.git Shared/skills/sources/offensive-claude
git submodule add https://github.com/thananon/9arm-skills.git Shared/skills/sources/9arm-skills
git submodule add https://github.com/smixs/osint-skill.git Shared/skills/sources/osint-skill
```

Then build the local skill index:

```bash
./Shared/skills/ko-ai-pentest/scripts/build-ko-skill-index.sh
```

## Reporting Rules

The main report for every target is:

```text
reports/pentest-report-final.md
```

Ko must log every meaningful action immediately:

- timestamp
- command/action
- reason
- how it helped
- result summary
- evidence path
- finding relationship
- next step

## Final Finding Sorting Rule

When finalizing a report, Ko must:

1. Collect all findings from existing evidence.
2. Sort by severity first:
   - Critical
   - High
   - Medium
   - Low
   - Informational
   - Positive / Passed
3. After sorting, assign final IDs:
   - F-001
   - F-002
   - F-003
4. Preserve old IDs as `Original ID`.

## Credential Handling

Optional credentials may be placed in:

```text
Shared/credentials/<client>/<name>.env
```

Then symlink into a target:

```bash
mkdir -p targets/<TARGET>/secrets
ln -sf ~/Desktop/AI_By_Ko/Shared/credentials/<client>/<name>.env targets/<TARGET>/secrets/credentials.env
```

Rules:

- Never commit credentials.
- Never print plaintext passwords in reports.
- Redact secrets as `[REDACTED]`.
- Ask before any state-changing authenticated action.

## GitHub Safety

The `.gitignore` blocks:

- secrets
- `.env` files
- evidence
- scan output
- temp files
- reports/final exports

Review before pushing.

## Typical Workflow

```text
Install template
↓
Create client workspace
↓
Add scope
↓
Create target
↓
Run Claude Code in target folder
↓
Ko reads CLAUDE.md + scope + skills
↓
Ko performs safe authorized assessment
↓
Ko logs everything to pentest-report-final.md
↓
Ko writes findings and dashboard status
↓
Ko finalizes severity-sorted report
```
