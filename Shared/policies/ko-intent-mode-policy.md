
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

