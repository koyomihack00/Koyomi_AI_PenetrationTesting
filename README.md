# Ko AI Pentest Framework

![Claude Code](https://img.shields.io/badge/Claude-Code-orange)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Mode](https://img.shields.io/badge/Modes-Work%20%7C%20Web%20%7C%20CTF%20%7C%20BugBounty%20%7C%20Lab-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-yellow)
![Security](https://img.shields.io/badge/Use-Authorized%20Testing%20Only-red)

Ko AI Pentest Framework is a Claude Code-driven penetration testing workspace designed for authorized security assessments, web application testing, client work, CTFs, bug bounty programs, and lab environments.

The framework provides a reusable structure for managing scope, targets, evidence, findings, reports, skills, policies, and assessment workflows.

The long-term vision is simple:

```text
Open Claude Code
Type: Pentest example.com
Ko handles the workflow
```

or:

```text
Open Claude Code
Type: Pentest 192.168.1.10
Ko handles the workflow
```

Ko is designed to help with:

- Target workspace creation
- Scope validation
- Skill selection
- Safe assessment workflow
- Evidence tracking
- Finding management
- Report generation
- Severity-based final reporting
- BurpSuite MCP-assisted web testing
- Multi-mode assessment workflows

---

## Table of Contents

- [Ko AI Pentest Framework](#ko-ai-pentest-framework)
  - [Overview](#overview)
  - [Project Vision](#project-vision)
  - [Current Status](#current-status)
  - [Key Features](#key-features)
  - [Architecture](#architecture)
  - [Assessment Workflow](#assessment-workflow)
  - [Full Workflow](#full-workflow)
  - [Project Structure](#project-structure)
  - [Core Components](#core-components)
  - [Ko Core Engine](#ko-core-engine)
  - [CLAUDE.md](#claudemd)
  - [Skill System](#skill-system)
  - [Mode System](#mode-system)
  - [BurpSuite MCP Support](#burpsuite-mcp-support)
  - [Installation](#installation)
  - [Git Submodules](#git-submodules)
  - [Create a Client Workspace](#create-a-client-workspace)
  - [Create a Target](#create-a-target)
  - [Run Ko with Claude Code](#run-ko-with-claude-code)
  - [Intent Mode Usage](#intent-mode-usage)
  - [Run Ko Core Manually](#run-ko-core-manually)
  - [Target Folder Structure](#target-folder-structure)
  - [Evidence Management](#evidence-management)
  - [Finding Management](#finding-management)
  - [Reporting](#reporting)
  - [Severity Sorting](#severity-sorting)
  - [Default Traffic Profile](#default-traffic-profile)
  - [Credential Handling](#credential-handling)
  - [Approval Gates](#approval-gates)
  - [Safety Model](#safety-model)
  - [What Ko Should Do Automatically](#what-ko-should-do-automatically)
  - [What Ko Must Ask Before Doing](#what-ko-must-ask-before-doing)
  - [GitHub Workflow](#github-workflow)
  - [Do Not Commit](#do-not-commit)
  - [Current Limitations](#current-limitations)
  - [Roadmap](#roadmap)
  - [FAQ](#faq)
  - [Security Notice](#security-notice)
  - [License](#license)

---

## Overview

Ko AI Pentest Framework is a structured assessment framework built around Claude Code.

It is not just a folder template. It is designed as a workflow framework that combines:

- Claude Code project instructions
- Per-target workspaces
- Reusable prompts
- Assessment modes
- Skill source integration
- Ko Core orchestration
- Report generation
- Evidence tracking
- Finding normalization
- Severity sorting

The framework is intended for professional and authorized use only.

---

## Project Vision

The intended user experience is:

```bash
cd ~/Desktop/AI_By_Ko/Work/CLIENT_NAME
claude
```

Then inside Claude Code:

```text
Pentest example.com
```

or:

```text
Pentest 192.168.1.10
```

Ko should then:

1. Understand the user intent.
2. Extract the target.
3. Identify or create the target workspace.
4. Read `CLAUDE.md`.
5. Confirm scope.
6. Load existing evidence.
7. Select relevant skills.
8. Continue safe assessment.
9. Log actions.
10. Update findings.
11. Update the dashboard.
12. Generate a final report.
13. Pause only for high-risk actions or Critical/High impact decisions.

---

## Current Status

| Component | Status |
|---|---|
| Workspace structure | Implemented |
| Client workspace template | Implemented |
| Target workspace template | Implemented |
| CLAUDE.md-driven workflow | Implemented |
| Scope-first assessment logic | Implemented |
| Ko Core engine | Implemented |
| Skill loader | Implemented |
| Skill optimizer | Implemented |
| Router | Implemented |
| Decision engine | Implemented |
| Finding engine | Implemented |
| Report engine | Implemented |
| Severity sorting | Implemented |
| BurpSuite MCP policy | Implemented |
| BurpSuite MCP detector | Implemented |
| Multi-mode support | Implemented |
| Intent Mode policy | Implemented |
| Fully autonomous exploit agent | Not intended |
| Safe autonomous assessment | Partially implemented |
| Human approval for risky actions | Required |

Ko is designed to assist and automate safe workflow operations. It is not intended to perform unrestricted exploitation or unauthorized activity.

---

## Key Features

- Claude Code-ready project structure
- Scope-first assessment workflow
- Per-target isolation
- Multi-client support
- Multi-mode operation
- Ko Core orchestration engine
- Skill selection and optimization
- BurpSuite MCP integration policy
- Evidence tracking
- Finding tracking
- Report generation
- Severity-first finding sorting
- Final report ID renumbering
- Approval gate for risky actions
- Default browser-like traffic profile policy
- Credential redaction policy
- GitHub-ready reusable framework

---

## Architecture

The architecture flow:

```text
User
 │
 ▼
Claude Code
 │
 ▼
Ko Intent Mode
 │
 ▼
CLAUDE.md
 │
 ▼
Ko Core
 ├─ Skill Loader
 ├─ Skill Optimizer
 ├─ Skill Router
 ├─ Decision Engine
 ├─ Finding Engine
 └─ Report Engine
 │
 ▼
Assessment Workflow
 │
 ▼
Evidence
Findings
Reports
```
<p align="center">
  <img src="docs/images/architecture.png" width="1400">
</p>
---
[⬆ Back to Top](#table-of-contents)

---

## Assessment Workflow

The assessment workflow:
<p align="center">
  <img src="docs/images/assessment-workflow.png" width="1400">
</p>
---
[⬆ Back to Top](#table-of-contents)

---

## Full Workflow

Full workflow concept:

```text
User Input
   │
   ▼
Claude Code
   │
   ▼
Intent Parser
   │
   ▼
Workspace Resolver
   │
   ▼
Scope Validator
   │
   ▼
Ko Core
   │
   ├── Mode Detector
   ├── Skill Loader
   ├── Skill Optimizer
   ├── Router
   ├── Decision Engine
   ├── Finding Engine
   └── Report Engine
   │
   ▼
Assessment Workflow
   │
   ├── Recon
   ├── Web Review
   ├── TLS Review
   ├── Auth Review
   ├── Burp MCP Review
   └── Evidence Collection
   │
   ▼
Findings
   │
   ▼
Severity Sorting
   │
   ▼
Final Report
```
<p align="center">
  <img src="docs/images/full-workflow.png" width="1400">
</p>
---
[⬆ Back to Top](#table-of-contents)

---

## Project Structure

```text
Ko-AI-Pentest/
├── README.md
├── GITHUB_SETUP.md
├── LICENSE
├── SECURITY.md
├── install.sh
├── .gitignore
│
├── scripts/
│   ├── create-target.sh
│   └── ko-core-run.sh
│
├── ko-core/
│   ├── skill-loader.py
│   ├── skill-optimizer.py
│   ├── ko-router.py
│   ├── decision-engine.py
│   ├── finding-engine.py
│   ├── severity_engine.py
│   ├── report-engine.py
│   ├── workflow-engine.py
│   ├── mode-detector.py
│   └── burp-mcp-detector.py
│
├── Shared/
│   ├── prompts/
│   │   ├── resume-target.md
│   │   └── burp-assisted-web-pentest.md
│   │
│   ├── policies/
│   │   ├── autonomous-processing-policy.md
│   │   ├── ko-intent-mode-policy.md
│   │   ├── default-traffic-profile-policy.md
│   │   └── burpsuite-mcp-policy.md
│   │
│   ├── mcp/
│   │   └── burpsuite-mcp-template.json
│   │
│   ├── modes/
│   │   ├── work.md
│   │   ├── web.md
│   │   ├── ctf.md
│   │   ├── bugbounty.md
│   │   └── lab.md
│   │
│   ├── skills/
│   │   ├── ko-ai-pentest/
│   │   └── sources/
│   │       ├── offensive-claude/
│   │       ├── 9arm-skills/
│   │       └── osint-skill/
│   │
│   └── templates/
│       └── target-template/
│
└── templates/
    └── client/
```
---
[⬆ Back to Top](#table-of-contents)

---

## Core Components

### `install.sh`

Creates a new client workspace.

Example:

```bash
./install.sh ACME
```

Creates:

```text
~/Desktop/AI_By_Ko/Work/ACME/
```

---

### `scripts/create-target.sh`

Creates a new target workspace.

Example:

```bash
./scripts/create-target.sh 192.0.2.10
```

---

### `scripts/ko-core-run.sh`

Runs Ko Core against a target folder.

Example:

```bash
./scripts/ko-core-run.sh ~/Desktop/AI_By_Ko/Work/ACME/targets/192.0.2.10
```

---

## Ko Core Engine

Ko Core is the orchestration layer.

```text
ko-core/
├── skill-loader.py
├── skill-optimizer.py
├── ko-router.py
├── decision-engine.py
├── finding-engine.py
├── severity_engine.py
├── report-engine.py
├── workflow-engine.py
├── mode-detector.py
└── burp-mcp-detector.py
```

### `skill-loader.py`

Indexes available skills from configured skill sources.

Output:

```text
Shared/skills/ko-ai-pentest/references/KO_SKILL_INDEX.json
```

---

### `skill-optimizer.py`

Selects only the most relevant skills to reduce token usage.

Example selected skills:

```text
web-pentest
tls-review
auth-session-review
```

---

### `ko-router.py`

Detects target profile and suggests workflow direction.

---

### `decision-engine.py`

Classifies whether Ko should:

```text
AUTO_CONTINUE
PAUSE_FOR_HIGH_IMPACT_REVIEW
ASK_APPROVAL
```

---

### `finding-engine.py`

Parses findings and normalizes them.

---

### `severity_engine.py`

Sorts findings by severity and assigns final IDs.

---

### `report-engine.py`

Updates the final report.

Primary report:

```text
reports/pentest-report-final.md
```

---

### `workflow-engine.py`

Runs the Ko Core workflow.

---

### `mode-detector.py`

Detects assessment mode:

```text
work
web
ctf
bugbounty
lab
```

---

### `burp-mcp-detector.py`

Detects BurpSuite MCP availability.

Default endpoint:

```text
http://127.0.0.1:9876
```

[⬆ Back to Top](#table-of-contents)

---

## CLAUDE.md

`CLAUDE.md` is the operating manual for Claude Code inside each project or target workspace.

It defines:

- target context
- scope rules
- Rules of Engagement
- allowed actions
- denied actions
- approval gates
- reporting format
- finding format
- evidence handling
- credential handling
- mode behavior
- skill usage
- traffic profile
- Burp MCP behavior

Each target has its own:

```text
targets/TARGET/CLAUDE.md
```

This allows Ko to resume work even after changing Claude accounts, machines, sessions, or terminals.

[⬆ Back to Top](#table-of-contents)

---

## Skill System

Ko integrates external skill repositories through Git submodules.

Supported sources:

```text
Shared/skills/sources/offensive-claude/
Shared/skills/sources/9arm-skills/
Shared/skills/sources/osint-skill/
```

Unified Ko skill:

```text
Shared/skills/ko-ai-pentest/SKILL.md
```

Ko should not load all skill content blindly.

Skill optimization strategy:

1. Read the skill index first.
2. Select the top relevant skills.
3. Load only what is needed.
4. Reuse existing evidence.
5. Avoid duplicate scans.
6. Summarize long outputs into files.

[⬆ Back to Top](#table-of-contents)

---

## Mode System

Ko supports multiple assessment modes.

```text
Shared/modes/
├── work.md
├── web.md
├── ctf.md
├── bugbounty.md
└── lab.md
```

| Mode | Purpose |
|---|---|
| work | Authorized client pentest |
| web | Web application testing |
| ctf | Capture The Flag |
| bugbounty | Bug bounty program testing |
| lab | HTB, THM, local labs |

Modes influence:

- policy
- approval gates
- report format
- allowed actions
- workflow behavior
- selected skills

[⬆ Back to Top](#table-of-contents)

---

## BurpSuite MCP Support

Ko supports the PortSwigger Burp Suite MCP Server BApp extension.

Default endpoint:

```text
http://127.0.0.1:9876
```

Default mode:

```text
SSE MCP mode
```

Configuration template:

```text
Shared/mcp/burpsuite-mcp-template.json
```

Target template MCP file:

```text
Shared/templates/target-template/.mcp.json
```

Ko may use BurpSuite MCP to review:

- sitemap
- proxy history
- request/response pairs
- passive issues
- existing scanner issues
- endpoint behavior

Ko must ask before:

- active scanning
- Intruder usage
- Collaborator/OAST testing
- state-changing request replay
- exploitation
- accessing additional sensitive data

Burp evidence paths:

```text
targets/TARGET/evidence/burp/
targets/TARGET/scans/burp/
targets/TARGET/notes/burp-notes.md
```

[⬆ Back to Top](#table-of-contents)

---

## Installation

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

If already cloned without submodules:

```bash
git submodule update --init --recursive
```

Install a client workspace:

```bash
./install.sh CLIENT_NAME
```

Example:

```bash
./install.sh ACME
```

Creates:

```text
~/Desktop/AI_By_Ko/Work/ACME/
```

[⬆ Back to Top](#table-of-contents)

---

## Git Submodules

Add submodules:

```bash
git submodule add https://github.com/hypnguyen1209/offensive-claude.git Shared/skills/sources/offensive-claude
git submodule add https://github.com/thananon/9arm-skills.git Shared/skills/sources/9arm-skills
git submodule add https://github.com/smixs/osint-skill.git Shared/skills/sources/osint-skill
```

Initialize submodules:

```bash
git submodule update --init --recursive
```

Update submodules:

```bash
git submodule update --remote
```

[⬆ Back to Top](#table-of-contents)

---

## Create a Client Workspace

Install a workspace:

```bash
./install.sh ACME
```

Workspace path:

```text
~/Desktop/AI_By_Ko/Work/ACME/
```

Example structure:

```text
Work/ACME/
├── CLAUDE.md
├── LOCAL_SKILLS_INDEX.md
├── scope/
├── targets/
├── reports/
└── scripts/
```

[⬆ Back to Top](#table-of-contents)

---

## Create a Target

Go to the workspace:

```bash
cd ~/Desktop/AI_By_Ko/Work/ACME
```

Create a target:

```bash
./scripts/create-target.sh 192.0.2.10
```

Creates:

```text
targets/192.0.2.10/
```

[⬆ Back to Top](#table-of-contents)

---

## Run Ko with Claude Code

Go to the client workspace:

```bash
cd ~/Desktop/AI_By_Ko/Work/ACME
claude
```

Inside Claude Code:

```text
Pentest 192.0.2.10
```

or:

```text
Pentest example.com
```

Ko should load the local project instructions and continue the workflow.

[⬆ Back to Top](#table-of-contents)

---

## Intent Mode Usage

Ko Intent Mode is designed to interpret short user commands.

Examples:

```text
Pentest 192.168.1.10
Pentest example.com
Assess example.com
Test 10.10.10.10
CTF HTB-Machine
BugBounty example.com
```

Ko should:

1. Extract the target.
2. Detect mode if possible.
3. Locate or create target workspace.
4. Validate scope.
5. Run Ko Core.
6. Select relevant skills.
7. Continue safe assessment.
8. Log actions.
9. Update report.

[⬆ Back to Top](#table-of-contents)

---

## Run Ko Core Manually

Run Ko Core against a target:

```bash
./scripts/ko-core-run.sh ~/Desktop/AI_By_Ko/Work/ACME/targets/192.0.2.10
```

This performs:

1. mode detection
2. skill loading
3. skill optimization
4. routing
5. decision classification
6. finding parsing
7. report section generation

[⬆ Back to Top](#table-of-contents)

---

## Target Folder Structure

```text
targets/TARGET/
├── CLAUDE.md
├── scope/
│   ├── targets.txt
│   ├── roe.md
│   └── out-of-scope.txt
│
├── scans/
│   ├── recon/
│   ├── web/
│   ├── tls/
│   ├── vuln/
│   └── burp/
│
├── evidence/
│   └── burp/
│
├── findings/
│   ├── findings.md
│   └── findings.json
│
├── notes/
│   ├── status.md
│   └── burp-notes.md
│
├── dashboard/
│   ├── status.json
│   └── attack-map.json
│
├── reports/
│   └── pentest-report-final.md
│
├── scripts/
├── tmp/
├── .claude/
└── secrets/
```

[⬆ Back to Top](#table-of-contents)

---

## Evidence Management

Evidence should be stored under:

```text
evidence/
scans/
tmp/
```

Examples:

```text
evidence/http/
evidence/burp/
evidence/screenshots/
scans/recon/
scans/web/
scans/tls/
scans/vuln/
```

Evidence should be:

- minimal
- relevant
- redacted
- linked to findings
- referenced in the final report

[⬆ Back to Top](#table-of-contents)

---

## Finding Management

Findings are stored in:

```text
findings/findings.md
findings/findings.json
```

A finding should include:

- Finding ID
- Original ID
- Title
- Severity
- Resolution Status
- Risk Confirmed
- Description
- How Discovered
- Commands Used
- Evidence Paths
- Impact
- Recommendation
- Validation Status

[⬆ Back to Top](#table-of-contents)

---

## Reporting

Primary report:

```text
reports/pentest-report-final.md
```

Supporting files:

```text
findings/findings.md
notes/status.md
dashboard/status.json
```

Every meaningful action should be logged with:

- timestamp
- command or action
- reason
- result
- evidence path
- finding relationship
- next step

[⬆ Back to Top](#table-of-contents)

---

## Severity Sorting

Ko sorts findings by severity before assigning final IDs.

Severity order:

```text
Critical
High
Medium
Low
Informational
Positive
```

Then final IDs are assigned:

```text
F-001
F-002
F-003
...
```

Original IDs are preserved as:

```text
Original ID: F-xxx
```

This prevents finding numbers from being tied to discovery order.

[⬆ Back to Top](#table-of-contents)

---

## Default Traffic Profile

Ko should not identify traffic as:

- AI
- Claude
- Bot
- Automated Agent

Default behavior:

- Use a standard browser-like User-Agent.
- Keep it consistent.
- Record it in the report.
- Do not randomize headers unnecessarily.
- Do not use stealth/evasion unless explicitly authorized.

Default example:

```text
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0 Safari/537.36
```

[⬆ Back to Top](#table-of-contents)

---

## Credential Handling

Credentials should be stored only in:

```text
secrets/credentials.env
```

Rules:

- never commit credentials
- never print plaintext credentials
- never write passwords to reports
- redact as `[REDACTED]`
- use only with authorization
- ask before state-changing authenticated actions

[⬆ Back to Top](#table-of-contents)

---

## Approval Gates

Ko should ask before:

- exploitation
- credential testing
- brute force
- password spraying
- authentication bypass validation
- state-changing actions
- availability-impacting actions
- accessing additional sensitive data
- Critical or High impact follow-up decisions

Ko should not ask before routine safe actions.

[⬆ Back to Top](#table-of-contents)

---

## Safety Model

Ko is designed for:

- authorized testing
- scoped assessments
- non-destructive validation
- evidence-driven findings
- human approval for risky actions
- professional reporting

Ko is not designed for:

- unauthorized testing
- malware deployment
- destructive exploitation
- credential theft
- persistence
- DoS
- unrestricted autonomous exploitation

[⬆ Back to Top](#table-of-contents)

---

## What Ko Should Do Automatically

Ko may continue automatically for:

- scope review
- evidence review
- skill selection
- safe recon
- service discovery
- HTTP review
- HTTPS review
- TLS review
- header review
- cookie review
- source review
- version review
- non-intrusive validation
- evidence collection
- notes update
- dashboard update
- report update

[⬆ Back to Top](#table-of-contents)

---

## What Ko Must Ask Before Doing

Ko must ask before:

- exploitation
- credential testing
- brute force
- password spraying
- auth bypass validation
- state-changing requests
- active scanning that may impact availability
- destructive testing
- accessing additional sensitive data
- Critical or High impact follow-up validation

[⬆ Back to Top](#table-of-contents)

---

## GitHub Workflow

Check status:

```bash
git status
```

Stage files:

```bash
git add .
```

Commit:

```bash
git commit -m "Update Ko AI Pentest Framework"
```

Push:

```bash
git push
```

[⬆ Back to Top](#table-of-contents)

---

## Do Not Commit

Never commit:

- credentials
- `.env`
- tokens
- secrets
- screenshots from real engagements
- evidence from real engagements
- scan output from real engagements
- client reports
- sensitive customer data
- API keys
- session cookies
- authentication tokens

Recommended `.gitignore` entries:

```text
**/secrets/
**/*.env
**/evidence/
**/scans/
**/tmp/
**/screenshots/
**/*.har
**/*.pcap
**/*.pcapng
**/reports/final/
.claude/
```

[⬆ Back to Top](#table-of-contents)

---

## Current Limitations

Current limitations:

- depends on Claude Code
- not a fully autonomous exploit agent
- external tool execution still depends on Claude Code permissions
- high-risk actions require human approval
- skill selection is keyword/profile based
- report generation depends on available evidence quality
- mode detection may require folder/project context
- BurpSuite MCP depends on Burp extension availability

[⬆ Back to Top](#table-of-contents)

---

## Roadmap

Planned improvements:

- stronger intent parser
- richer mode detection
- better workflow automation
- improved skill ranking
- evidence deduplication
- report quality scoring
- Burp MCP evidence import helpers
- mobile mode
- cloud mode
- Active Directory mode
- API pentest mode
- better dashboard rendering
- HTML/PDF report export
- target lifecycle manager

[⬆ Back to Top](#table-of-contents)

---

## FAQ

### Can I use this for client work?

Yes, if you have written authorization and proper scope.

### Can I use this for web pentesting?

Yes. Web mode, web-pentest skills, TLS review, auth review, and BurpSuite MCP support are designed for web assessments.

### Can I use this for CTF?

Yes. Use CTF or Lab mode.

### Does Ko automatically exploit targets?

No. Risky actions require approval.

### Does Ko support BurpSuite MCP?

Yes. The framework supports the PortSwigger BurpSuite MCP Server extension at:

```text
http://127.0.0.1:9876
```

### Does Ko store findings?

Yes. Findings are stored under:

```text
findings/
```

### Does Ko generate a final report?

Yes. The main report file is:

```text
reports/pentest-report-final.md
```

### Can I change Claude accounts?

Yes. Project memory is stored in local files such as `CLAUDE.md`, reports, findings, notes, dashboard, and evidence.

### Can I move the project to another machine?

Yes, if you move the workspace and repository files. Reinitialize submodules if needed.

[⬆ Back to Top](#table-of-contents)

---

## Security Notice

This framework is intended only for authorized security assessments.

Users are responsible for ensuring they have written permission before testing any target.

Do not use this framework against systems you do not own or do not have authorization to assess.

Unauthorized testing is prohibited.

[⬆ Back to Top](#table-of-contents)

---

## License

Refer to the `LICENSE` file for licensing information.

[⬆ Back to Top](#table-of-contents)
