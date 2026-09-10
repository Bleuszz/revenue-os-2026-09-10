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
| Payment connector | PARTIAL | No payment MCP tool is callable; payment collection therefore needs a user-controlled browser/account route |
| Stripe browser session | INACTIVE | Authenticated in sandbox mode, but live activation requires unavailable photo-ID/selfie verification; do not depend on it |
| PayPal | UNVERIFIED | No account state was inspected or changed; use only an existing account already able to receive and release commercial funds without document verification |
| Direct UK bank transfer | CONDITIONAL | Preferred after buyer agreement; Nathan supplies details at that point and receipt must be verified in the actual bank account |
| OpenAI API key | AVAILABLE | Environment variable name present; value not inspected or recorded |
| Codex usage | AVAILABLE | Weekly bucket 1% used; no paid credits at audit |
| Available task models | AVAILABLE | Host exposes GPT-6 Astra, GPT-5.6 Sol, GPT-5.6 Terra, GPT-5.6 Luna, GPT-5.5, and GPT-5.3-Codex-Spark with model-specific reasoning levels |
| Additional capital | AVAILABLE | £30 maximum; £0 spent |
| Continuation heartbeat | ACTIVE | `seven-day-revenue-mission`; resumes about every four hours through the deadline and stays quiet when nothing actionable changes |

## Constraints

- The current session cannot change its own model.
- External revenue requires a real buyer and a user-owned way to accept payment.
- Assume no photo ID is available. Do not create or depend on services requiring identity documents unless completely necessary and Nathan explicitly changes the constraint.
- No new account has been created.
- No credentials, bank details, mailbox content, identity material, or tokens are stored in this repository.
