Resume this authorized target assessment.

Read and follow:
- CLAUDE.md
- scope/*
- notes/status.md
- dashboard/status.json
- findings/*
- reports/*
- scans/*
- evidence/*
- ~/Desktop/AI_By_Ko/Work/*/LOCAL_SKILLS_INDEX.md if available
- ~/Desktop/AI_By_Ko/Shared/skills/ko-ai-pentest/SKILL.md

Use existing evidence first.
Do not repeat completed work.
Do not run duplicate scans.

Proceed automatically for safe recon, fingerprinting, TLS/header/cookie review, documentation, dashboard updates, and report updates.

Log every meaningful action to reports/pentest-report-final.md with command/action, reason, how it helped, result, evidence path, finding relationship, and next step.

Ask only before exploitation, credential testing, brute force, password spraying, auth bypass testing, state-changing actions, or availability-impacting actions.

When finalizing the report:
- Rebuild findings from source evidence.
- Sort by severity: Critical > High > Medium > Low > Informational > Positive.
- Then assign final IDs sequentially: F-001, F-002, F-003.
- Preserve original IDs as Original ID.
- Keep raw logs intact.

If no additional safe work remains, finalize reports/pentest-report-final.md, findings/findings.md, notes/status.md, dashboard/status.json, and stop.
