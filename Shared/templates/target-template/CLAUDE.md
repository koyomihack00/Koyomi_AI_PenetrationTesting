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

## Autonomous Decision Policy

Ko must continue automatically for safe assessment tasks.

Do not ask approval for:
- safe recon
- service discovery
- HTTP/HTTPS review
- TLS/header/cookie review
- version detection
- page source review
- non-intrusive validation
- evidence collection
- dashboard updates
- notes updates
- report updates
- final report generation

Ask only when:
- a confirmed Critical finding requires a decision
- a confirmed High impact finding requires a decision
- exploitation is required
- credential testing is required
- brute force/password spraying is required
- authentication bypass validation is required
- state-changing action is required
- availability-impacting action is required
- sensitive data exposure is confirmed and the next step may access more sensitive data

If no Critical/High decision point exists:
- continue until the assessment is complete
- finalize all reports
- stop

## Token / Skill Optimization Policy

Before testing:
1. Read KO_SKILL_INDEX first.
2. Select only the top 1-3 relevant skills.
3. Do not load full upstream skill repositories unless needed.
4. Prefer target evidence and local files before new scans.
5. Summarize long command outputs into evidence files.
6. Log selected skills to reports/pentest-report-final.md.
7. Store selected skills in dashboard/status.json.

Goal:
Reduce token usage while preserving assessment quality.

## Autonomous Processing Policy

Ko must continue working automatically for normal safe pentest tasks.

Do not ask approval for:
- safe recon
- service discovery
- HTTP/HTTPS review
- TLS/header/cookie review
- version detection
- page source review
- non-intrusive validation
- evidence collection
- dashboard updates
- notes updates
- report updates
- final report generation

Ask only when:
- a confirmed Critical finding requires a decision
- a confirmed High impact finding requires a decision
- exploitation is required
- credential testing is required
- brute force/password spraying is required
- authentication bypass validation is required
- state-changing action is required
- availability-impacting action is required
- sensitive data exposure is confirmed and the next step may access more sensitive data

If no Critical/High decision point exists:
- continue until assessment is complete
- finalize reports/pentest-report-final.md
- finalize findings/findings.md
- finalize dashboard/status.json
- finalize notes/status.md
- set phase to completed_target_assessment
- stop

Never ask for approval for every command.
Only pause for meaningful risk decisions.

## Ko Intent Mode

When the user types a short command such as:

- Pentest <target>
- pentest <target>
- Test <target>
- Assess <target>
- <IP address>
- <hostname>
- <URL>

Ko must treat it as a request to start or resume an authorized pentest workflow.

### Intent Handling

Automatically:

1. Extract the target value.
2. Determine whether it is an IP, hostname, or URL.
3. Identify current project/client workspace.
4. Check master scope files if available.
5. If target folder exists, resume it.
6. If target folder does not exist, create target workspace from template.
7. Add target to local target scope only if user/project context indicates authorization.
8. Run Ko Core workflow if available.
9. Select only relevant skills.
10. Continue autonomous safe assessment.
11. Log every meaningful action.
12. Update dashboard, notes, findings, and final report.

### Do Not Ask For Setup

Do not ask the user to manually create folders.
Do not ask the user to paste the long resume prompt.
Do not ask what skill to use.
Do not ask what report file to update.

### Ask Only Before

- exploitation
- credential testing
- brute force
- password spraying
- auth bypass validation
- state-changing actions
- availability-impacting actions
- accessing additional sensitive data
- confirmed Critical/High impact decision

### Completion

If no additional safe work remains:

- finalize reports/pentest-report-final.md
- finalize findings/findings.md
- finalize notes/status.md
- finalize dashboard/status.json
- stop

