
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
