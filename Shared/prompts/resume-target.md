Resume this authorized target.

Read and follow:
- CLAUDE.md
- scope/*
- notes/status.md
- dashboard/status.json
- findings/*
- reports/*
- scans/*
- evidence/*
- LOCAL_SKILLS_INDEX.md
- Shared/skills/ko-ai-pentest/SKILL.md if available

Operate autonomously according to CLAUDE.md.

Use existing evidence first.
Do not repeat completed work.
Do not run duplicate scans.

Before testing:
- select only top relevant skills
- do not load all skill sources
- log selected skills in reports/pentest-report-final.md
- update dashboard/status.json

Continue automatically for safe assessment:
- recon
- service discovery
- HTTP/HTTPS review
- TLS/header/cookie review
- version detection
- source review
- non-intrusive validation
- evidence collection
- report updates
- dashboard updates
- notes updates

Ask only before:
- Critical/High impact decision
- exploitation
- credential testing
- brute force
- password spraying
- auth bypass validation
- state-changing actions
- availability-impacting actions
- accessing additional sensitive data

Mandatory:
- Log every meaningful action to reports/pentest-report-final.md
- Include command/action, reason, result, evidence path, finding relationship, and next step
- Keep dashboard and notes updated

When updating the final report:
- rebuild findings from source evidence
- sort findings by severity first:
  Critical > High > Medium > Low > Informational > Positive
- then assign final IDs sequentially:
  F-001, F-002, F-003...
- preserve original IDs as Original ID
- keep raw logs intact

If no additional safe work remains:
- finalize reports/pentest-report-final.md
- finalize findings/findings.md
- finalize notes/status.md
- finalize dashboard/status.json
- set phase to completed_target_assessment
- stop

Autonomous processing rule:
Continue automatically for safe assessment work.
Do not ask approval for every command.
Pause only for confirmed Critical/High impact decisions or risky actions such as exploitation, credential testing, brute force, auth bypass validation, state-changing actions, availability-impacting actions, or accessing additional sensitive data.
