# Ko AI Target Workspace

This folder is one isolated target assessment workspace.

## Mandatory Startup

Read:

- `CLAUDE.md`
- `scope/targets.txt`
- `scope/out-of-scope.txt`
- `scope/roe.md`
- `notes/status.md`
- `dashboard/status.json`
- `reports/pentest-report-final.md`
- `findings/findings.md`
- `scans/`
- `evidence/`
- `tmp/`
- `~/Desktop/AI_By_Ko/Shared/skills/ko-ai-pentest/SKILL.md`

## Scope Rule

Test only the target listed in `scope/targets.txt` and only when it is also approved in the master project scope.

## Autonomous Safe Work

Proceed automatically for:

- safe recon
- service discovery
- fingerprinting
- TLS/certificate review
- HTTP/header/cookie review
- login/source review
- non-destructive vulnerability triage
- evidence collection
- dashboard updates
- notes updates
- report updates

## Approval Gate

Ask before:

- exploitation
- credential testing
- default credential testing
- brute force
- password spraying
- auth bypass testing
- state-changing actions
- availability-impacting actions

## Mandatory Live Logging

Every meaningful action must be appended immediately to:

`reports/pentest-report-final.md`

Include:

- timestamp
- command/action
- reason
- how it helped
- result summary
- evidence path
- finding relationship
- next step

## Skill Usage Logging

When skills or agents are selected, write them to:

`reports/pentest-report-final.md`

Include:

- name
- purpose
- phase used
- why selected
- whether evidence was produced

## Final Report Sorting

When finalizing `reports/pentest-report-final.md`:

1. Collect all findings.
2. Sort by severity first:
   - Critical
   - High
   - Medium
   - Low
   - Informational
   - Positive / Passed
3. Assign new final IDs only after sorting:
   - F-001
   - F-002
   - F-003
4. Preserve original IDs as `Original ID`.
5. Keep raw logs intact.

## Credential Handling

If `secrets/credentials.env` exists:

- Use only if the target accepts the approved account.
- Never print plaintext credentials.
- Never write passwords to reports/findings.
- Redact secrets as `[REDACTED]`.
- Ask before account modification or state-changing authenticated actions.
