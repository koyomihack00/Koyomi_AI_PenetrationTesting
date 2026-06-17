## BurpSuite MCP Integration Policy

Ko supports the PortSwigger Burp Suite MCP Server BApp extension.

Default Burp MCP endpoint:

http://127.0.0.1:9876

Mode:

SSE MCP mode

Allowed Burp-assisted actions:
- Read Burp sitemap
- Read HTTP proxy history
- Review request/response pairs
- Review passive issues
- Review scanner issues already created by the operator
- Create Repeater tabs for manual review
- Correlate Burp evidence with findings
- Save sanitized evidence under evidence/burp/
- Save summaries under scans/burp/
- Update notes/burp-notes.md
- Update reports/pentest-report-final.md

Do not automatically:
- Start active scans
- Use Intruder attacks
- Perform brute force
- Replay state-changing requests
- Modify data
- Upload files
- Exploit findings
- Access additional sensitive data
- Generate out-of-band payloads without approval

Ask before:
- active scanning
- Intruder
- Collaborator / OAST testing
- request replay that may change state
- scanner actions that may impact availability
- Critical or High impact follow-up validation

Evidence handling:
- Redact cookies
- Redact tokens
- Redact Authorization headers
- Redact session IDs
- Redact PII
- Redact secrets

All Burp-assisted actions must be logged in:

reports/pentest-report-final.md
