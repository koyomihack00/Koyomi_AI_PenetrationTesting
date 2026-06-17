# Ko AI Pentest Framework

Ko AI Pentest Framework is a Claude Code-ready workspace template for authorized penetration testing engagements.

## Features

- Client workspace structure
- Per-target folders
- Scope and ROE controls
- Claude Code permissions
- Unified Ko AI pentest skill
- Live reporting
- Evidence tracking
- Severity-sorted final reports

## Included Skill Sources

This project can integrate these Git submodules:

- offensive-claude
- 9arm-skills
- osint-skill

Submodules path:

Shared/skills/sources/

## Install

git clone --recurse-submodules <YOUR_REPO_URL>
cd Ko-AI-Pentest
./install.sh CLIENT_NAME

Example:

./install.sh ACME

## Create Target

cd ~/Desktop/AI_By_Ko/Work/ACME
./scripts/create-target.sh 192.0.2.10

## Run Ko

cd ~/Desktop/AI_By_Ko/Work/ACME/targets/192.0.2.10
claude "$(cat ~/Desktop/AI_By_Ko/Shared/prompts/resume-target.md)"

## Primary Report

reports/pentest-report-final.md

## Finding Order

Critical > High > Medium > Low > Informational > Positive

Final IDs are assigned after severity sorting:

F-001, F-002, F-003

## Safety

Authorized testing only.

Do not use against systems without written permission.

Never commit:

- credentials
- .env files
- tokens
- evidence
- scan outputs
- real client reports

## Ko Core Engine

Ko Core Engine adds lightweight orchestration:

- skill-loader
- ko-router
- finding-engine
- severity-engine
- report-engine
- workflow-engine

Run Ko Core against a target:

    ./scripts/ko-core-run.sh ~/Desktop/AI_By_Ko/Work/CLIENT_NAME/targets/TARGET

Ko Core will:
1. index skills
2. select relevant skills
3. parse findings
4. sort findings by severity
5. renumber final finding IDs
6. update reports/pentest-report-final.md

## Autonomous Decision + Token Optimization

Ko is designed to continue automatically for safe pentest tasks and only pause when a high-impact decision is required.

Auto-continue tasks:
- recon
- service discovery
- HTTP/HTTPS review
- TLS/header/cookie review
- source review
- version detection
- non-intrusive validation
- evidence collection
- report update

Ko asks before:
- Critical/High impact decision
- exploitation
- credential testing
- brute force/password spray
- auth bypass validation
- state-changing action
- availability-impacting action
- accessing additional sensitive data

Skill optimization:
- Ko reads the skill index first
- selects only top 1-3 relevant skills
- avoids loading all upstream repositories
- stores selected skills in dashboard/status.json
- logs selected skills in reports/pentest-report-final.md

Run Ko Core:

    ./scripts/ko-core-run.sh <TARGET_FOLDER>
