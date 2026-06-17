
## Default Traffic Profile Policy

Ko must not identify traffic as AI, Claude, bot, or automated pentest agent.

Do not use User-Agent strings such as:
- Ko-AI-Pentest
- Claude-Code-Agent
- AI-Pentest-Bot
- OpenAI-Agent

Default behavior:
- Use a standard browser-like User-Agent.
- Keep the User-Agent consistent during the assessment.
- Record the User-Agent used in reports/pentest-report-final.md.
- Do not randomize headers unless explicitly required by the test objective.
- Do not use stealth, evasion, or anti-detection behavior unless explicitly authorized.

Default User-Agent:

Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0 Safari/537.36

For curl/http tools, use:

-H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0 Safari/537.36"
