# Ko AI Pentest Framework

Ko AI Pentest Framework is a Claude Code-ready penetration testing workspace for authorized security assessments.

It provides a reusable project structure, target isolation, scope control, skill routing, autonomous safe assessment workflow, evidence tracking, and final report generation.

This project is intended for professional, authorized penetration testing only.

---

## Key Features

- Client workspace template
- Per-target folder isolation
- Scope-first workflow
- Rules of Engagement enforcement
- Claude Code permission policy
- Ko AI unified pentest skill
- Skill source submodules
- Auto skill selection
- Token-saving skill optimization
- Autonomous safe assessment mode
- Approval gate for high-risk actions
- Evidence collection
- Finding tracking
- Severity sorting
- Final report generation
- GitHub-ready reusable template

---

## Included Skill Sources

This project integrates external skill sources as Git submodules:

- offensive-claude
- 9arm-skills
- osint-skill

Submodule path:

Shared/skills/sources/

Unified Ko skill path:

Shared/skills/ko-ai-pentest/SKILL.md

---

## Main Project Structure

Ko-AI-Pentest/
├── README.md
├── GITHUB_SETUP.md
├── install.sh
├── .gitignore
├── scripts/
│   ├── create-target.sh
│   └── ko-core-run.sh
├── ko-core/
│   ├── skill-loader.py
│   ├── skill-optimizer.py
│   ├── ko-router.py
│   ├── decision-engine.py
│   ├── finding-engine.py
│   ├── severity_engine.py
│   ├── report-engine.py
│   └── workflow-engine.py
├── Shared/
│   ├── prompts/
│   │   └── resume-target.md
│   ├── policies/
│   │   └── autonomous-processing-policy.md
│   ├── skills/
│   │   ├── ko-ai-pentest/
│   │   └── sources/
│   └── templates/
└── templates/
    └── client/

---

## Install

Clone with submodules:

git clone --recurse-submodules https://github.com/YOUR_USERNAME/YOUR_REPO.git

cd YOUR_REPO

Install a client workspace:

./install.sh CLIENT_NAME

Example:

./install.sh ACME

This creates:

~/Desktop/AI_By_Ko/Work/ACME/

---

## Create a Target

Go to the client workspace:

cd ~/Desktop/AI_By_Ko/Work/ACME

Create a new target:

./scripts/create-target.sh 192.0.2.10

This creates:

targets/192.0.2.10/

Target folder structure:

targets/TARGET/
├── CLAUDE.md
├── scope/
├── scans/
├── evidence/
├── findings/
├── notes/
├── dashboard/
├── reports/
├── scripts/
├── tmp/
├── .claude/
└── secrets/

---

## What CLAUDE.md Does

CLAUDE.md is the operating manual for Ko/Claude Code.

It defines:

- target context
- scope rules
- Rules of Engagement
- allowed actions
- denied actions
- approval gates
- report format
- logging rules
- skill usage rules
- final finding sorting rules
- autonomous decision behavior

Every target has its own CLAUDE.md so each assessment can be resumed safely from its own folder.

---

## Run Ko on a Target

Enter the target folder:

cd ~/Desktop/AI_By_Ko/Work/ACME/targets/192.0.2.10

Run Ko Core first:

~/Desktop/Ko-AI-Pentest/Ko-AI-Pentest/scripts/ko-core-run.sh .

Then start Claude Code with the standard prompt:

claude "$(cat ~/Desktop/AI_By_Ko/Shared/prompts/resume-target.md)"

---

## Ko Core Engine

Ko Core Engine is the automation and orchestration layer.

It includes:

- skill-loader.py
- skill-optimizer.py
- ko-router.py
- decision-engine.py
- finding-engine.py
- severity_engine.py
- report-engine.py
- workflow-engine.py

Ko Core performs:

1. Skill indexing
2. Skill optimization
3. Target profile detection
4. Decision classification
5. Finding parsing
6. Severity sorting
7. Final report section generation

Run Ko Core:

./scripts/ko-core-run.sh TARGET_FOLDER

Example:

./scripts/ko-core-run.sh ~/Desktop/AI_By_Ko/Work/ACME/targets/192.0.2.10

---

## Autonomous Processing Behavior

Ko continues automatically for safe assessment tasks.

Ko does not ask approval for:

- safe recon
- service discovery
- HTTP review
- HTTPS review
- TLS review
- header review
- cookie review
- version detection
- page source review
- non-intrusive validation
- evidence collection
- dashboard updates
- notes updates
- report updates
- final report generation

Ko asks before:

- Critical or High impact decision
- exploitation
- credential testing
- brute force
- password spraying
- authentication bypass validation
- state-changing actions
- availability-impacting actions
- accessing additional sensitive data

Goal:

Ko should not ask approval for every command. It should continue until it reaches a meaningful risk decision or completes the assessment.

---

## Skill Optimization

Ko avoids loading every skill source into context.

Optimization rules:

1. Read the skill index first.
2. Select only the top 1-3 relevant skills.
3. Avoid reading full upstream repositories unless needed.
4. Prefer local evidence before new scans.
5. Summarize long outputs into files.
6. Log selected skills to reports/pentest-report-final.md.
7. Store selected skills in dashboard/status.json.

Example selected skills:

- web-pentest
- tls-review
- recon-osint
- auth-session-review

---

## Reporting

Primary report file:

reports/pentest-report-final.md

Ko logs every meaningful action into the report:

- timestamp
- command or action
- reason
- result
- evidence path
- finding relationship
- next step

The final report includes:

- Executive Summary
- Scope
- Skills / Agents Used
- Findings Summary
- Final Sorted Findings
- Detailed Findings
- Recommendations
- Evidence Index
- Commands / Activity Log
- Skipped / Blocked Actions
- Final Conclusion

---

## Finding Sorting Logic

Ko always sorts findings by severity before assigning final IDs.

Severity order:

1. Critical
2. High
3. Medium
4. Low
5. Informational
6. Positive

After sorting, Ko assigns final IDs:

F-001
F-002
F-003

Original IDs are preserved as:

Original ID: F-xxx

This prevents old finding order from affecting the final report.

---

## Scope Control

Master scope is stored in:

scope/targets.txt
scope/domains.txt
scope/roe.md
scope/out-of-scope.txt

Ko must confirm scope before testing.

If a target is not in scope:

- stop
- do not scan
- do not make requests
- report scope-blocked

---

## Credentials

Credentials are optional and must be stored only in:

secrets/credentials.env

Credential rules:

- never commit credentials
- never write passwords to reports
- never print plaintext secrets
- redact as [REDACTED]
- use only with written authorization

---

## GitHub Submodules

Initialize submodules:

git submodule update --init --recursive

Add submodules:

git submodule add https://github.com/hypnguyen1209/offensive-claude.git Shared/skills/sources/offensive-claude
git submodule add https://github.com/thananon/9arm-skills.git Shared/skills/sources/9arm-skills
git submodule add https://github.com/smixs/osint-skill.git Shared/skills/sources/osint-skill

Clone with submodules:

git clone --recurse-submodules REPO_URL

---

## Do Not Commit

Never commit:

- credentials
- .env files
- tokens
- secrets
- evidence
- scan output
- screenshots
- real client reports
- exploit output
- sensitive customer data

---

## Safety Notice

This framework is for authorized security testing only.

Do not use it against systems you do not own or do not have written permission to assess.

The framework is designed to support safe, scoped, professional penetration testing workflows.

---

## Ko Intent Mode

Preferred usage:

    cd ~/Desktop/AI_By_Ko/Work/CLIENT_NAME
    claude

Then inside Claude Code:

    Pentest 192.168.1.10

or:

    Pentest example.com

Ko will automatically:

1. Extract the target.
2. Check or create the target workspace.
3. Confirm scope.
4. Run Ko Core if available.
5. Select relevant skills.
6. Continue safe assessment.
7. Log every action.
8. Update dashboard, notes, findings, and report.
9. Pause only for Critical/High impact decisions or risky actions.
10. Finalize reports/pentest-report-final.md.

