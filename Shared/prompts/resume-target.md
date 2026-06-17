Ko AI Pentest Mode is active.

If the user provides:
- Pentest <target>
- pentest <target>
- Test <target>
- Assess <target>
- an IP address
- a hostname
- a URL

treat it as a request to start or resume an authorized pentest workflow.

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

Do not ask for setup steps.

Automatically:
1. Extract target.
2. Confirm scope.
3. Create target folder if missing.
4. Resume target if existing.
5. Run Ko Core if available.
6. Select only top relevant skills.
7. Continue safe assessment.
8. Log every meaningful action.
9. Update dashboard, notes, findings, and report.

Continue automatically for:
- safe recon
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
