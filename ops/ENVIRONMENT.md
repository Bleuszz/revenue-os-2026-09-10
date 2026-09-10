# Environment Audit

Audited: 2026-09-10 19:15 Europe/London

| Capability | Status | Evidence / constraint |
|---|---|---|
| Current date/time | AVAILABLE | 2026-09-10 19:09 BST at audit |
| Seven-day deadline | AVAILABLE | 2026-09-17 19:09 BST |
| Project directory | AVAILABLE | Local Codex projectless workspace |
| Git | AVAILABLE | Git installed; workspace initially not a repository |
| GitHub CLI | AVAILABLE | Authenticated; private repo scope present |
| GitHub connector | AVAILABLE | Authenticated profile; connector app has no listed installations, so CLI is preferred for repo creation |
| Gmail | AVAILABLE | Connected authorised account; profile verified |
| Internet research | AVAILABLE | Current official pages successfully fetched |
| Browser automation | AVAILABLE | In-app and named-browser control exposed |
| Local shell | AVAILABLE | PowerShell |
| Python | AVAILABLE | Python 3.12 |
| Node.js/npm | AVAILABLE | Installed |
| Deployment | AVAILABLE | Codex Sites connector; no site created |
| Vercel CLI | UNAVAILABLE | Not installed; no need identified |
| Payment connector | PARTIAL | No Stripe MCP tool is callable; an existing Stripe account is accessible through an authorised browser session |
| Stripe browser session | PARTIAL | Authenticated in sandbox mode; live activation is blocked on a user-only photo-ID and selfie verification step |
| OpenAI API key | AVAILABLE | Environment variable name present; value not inspected or recorded |
| Codex usage | AVAILABLE | Weekly bucket 1% used; no paid credits at audit |
| Available task models | AVAILABLE | Host exposes GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna, GPT-5.5, and GPT-5.3-Codex-Spark with model-specific reasoning levels |
| Additional capital | AVAILABLE | £30 maximum; £0 spent |
| Continuation heartbeat | ACTIVE | `seven-day-revenue-mission`; resumes about every four hours through the deadline and stays quiet when nothing actionable changes |

## Constraints

- The current session cannot change its own model.
- External revenue requires a real buyer and a user-owned way to accept payment.
- No new account has been created.
- No credentials, mailbox content, or tokens are stored in this repository.
