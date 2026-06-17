# Ko AI Client Workspace

This is the master workspace for an authorized pentest engagement.

## Startup Rules

Before testing any target:

1. Read master scope files.
2. Confirm target is in scope.
3. Read target `CLAUDE.md`.
4. Read `LOCAL_SKILLS_INDEX.md`.
5. Use the Ko AI unified skill.

## Unified Skill

Use:

- `~/Desktop/AI_By_Ko/Shared/skills/ko-ai-pentest/SKILL.md`
- `~/Desktop/AI_By_Ko/Shared/skills/ko-ai-pentest/references/KO_SKILL_INDEX.md`

## Reporting

Each target must write to:

`reports/pentest-report-final.md`

## Finding Sorting

Sort findings by severity first, then assign final IDs.

Severity order:

Critical > High > Medium > Low > Informational > Positive

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

