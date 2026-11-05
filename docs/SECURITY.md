# Sevenseas Broadband — Security Architecture & Controls Specification

## 1. Overview & Threat Model
Sevenseas Broadband operates as a residential fiber internet service provider. The primary web surface is a customer acquisition and lead generation platform. While the site does not process payments or store credit cards directly on this surface, it collects customer Personally Identifiable Information (PII) including names, telephone numbers, and residential society addresses.

**Threats Mitigated:**
* Automated spam bots and form stuffing
* Denial of Service (DoS) and volumetric API abuse
* Cross-Site Scripting (XSS) and Clickjacking
* SQL Injection (SQLi)
* Email Header Injection / SMTP relay spoofing
* Directory traversal and unauthorized lead exfiltration
* DNS / Email spoofing targeting subscribers

---

## 2. Transport & Website Security

### 2.1 HTTPS Enforcement & HSTS
* **Redirection:** All plaintext HTTP requests are redirected permanently (HTTP 301) to HTTPS.
* **HSTS Header:** Configured with a 2-year duration, subdomains inclusion, and preload eligibility:
  ```http
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  ```
* **TLS Version:** TLS 1.3 and TLS 1.2 enforced; legacy SSLv3, TLS 1.0, and TLS 1.1 disabled.

### 2.2 Content Security Policy (CSP) & Frame Protection
To prevent XSS and clickjacking:
```http
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://challenges.cloudflare.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' https://challenges.cloudflare.com; frame-src https://challenges.cloudflare.com; frame-ancestors 'none'; base-uri 'self'; form-action 'self';
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

### 2.3 Secret Management & Production Hardening
* **No Client Secrets:** Turnstile secret keys, database credentials, and email API keys reside strictly on the server (`process.env.TURNSTILE_SECRET_KEY`, `process.env.DATABASE_URL`, `process.env.RESEND_API_KEY`).
* **Source Control Guard:** `.gitignore` excludes `.env*`, `data/leads.db`, `data/leads.json`, and backup files.
* **Production Debugging Disabled:** Server error messages return generic, user-safe text without stack traces or internal filenames.

---

## 3. Form & Lead Generation Security

### 3.1 Defense-in-Depth Validation
1. **Client-Side:** Real-time formatting and validation for Indian mobile numbers (`^[6-9]\d{9}$`).
2. **Server-Side Zod Schema:** Independent validation enforcing length constraints, character sets, and plan enum membership (`lib/validation.ts`).
3. **Anti-Bot Honeypot:** Invisible `b_website` field. Bots populating this field are rejected.
4. **Cloudflare Turnstile:** Non-interactive, privacy-friendly bot challenge verified via server-side API call.
5. **Rate Limiting:** Sliding window limiter restricting clients to 5 enquiries per 15-minute window per IP. Exceeding triggers HTTP 429 Too Many Requests.
6. **SQL Injection Resistance:** Parameterized queries (`$1, $2, ...` in PostgreSQL; `?` in SQLite) completely disallow query structure tampering.
7. **Email Header Injection Prevention:** All inputs passing into notification emails are stripped of `\r`, `\n`, and control characters (`\x00-\x1f\x7f`) to prevent CRLF injection.
8. **XSS Escaping:** Input and output encoding for all rendered customer details.

---

## 4. Infrastructure & Network Security

### 4.1 Cloudflare DNS & WAF Configuration
For production deployment, Cloudflare proxying (Orange Cloud) is recommended:
* **WAF Managed Rules:** Enable Cloudflare Managed Ruleset (OWASP Core Ruleset, Score Threshold: Medium).
* **Bot Fight Mode:** Enabled to challenge automated scrapers.
* **Rate Limiting Rule:** Limit requests to `/api/enquiry` to 5 requests per 10 minutes per IP with a 15-minute block.
* **Country Filtering:** If desired, challenge requests originating from outside the operating region.

### 4.2 Email Authentication (Anti-Spoofing)
To guarantee deliverability and prevent phishing in Sevenseas' name:
* **SPF (Sender Policy Framework):**
  ```text
  v=spf1 include:_spf.resend.com ~all
  ```
* **DKIM (DomainKeys Identified Mail):** 2048-bit cryptographic key published in DNS.
* **DMARC (Domain-based Message Authentication):**
  ```text
  v=DMARC1; p=reject; rua=mailto:dmarc-reports@sevenseasbroadband.in; pct=100;
  ```

### 4.3 Lead Storage Isolation & Automated Backups
* **Private Directory Restriction:** Web server rules in `_headers`, `.htaccess`, and `nginx.conf` forbid direct HTTP access to `/data/` and `/config/`.
* **Automated Daily Backups:** [`scripts/backup_leads.py`](file:///Users/pratish/Desktop/Sevenseas%20Broadband/scripts/backup_leads.py) takes daily snapshots with SHA-256 checksum manifests and purges files older than 30 days.

### 4.4 Administrative Access & Two-Factor Authentication (2FA)
* **Hosting Accounts:** Vercel, Cloudflare, and domain registrars must enforce Hardware Security Key (FIDO2/WebAuthn) or TOTP Authenticator apps. SMS-based 2FA is discouraged.
* **Database Access:** PostgreSQL instances must run in private VPC networks with TLS enforced and password authentication rotated every 90 days.

### 4.5 Monitoring & Incident Response
* **Uptime Monitoring:** External polling every 60 seconds (e.g. UptimeRobot, Better Uptime) targeting `https://sevenseasbroadband.in/`.
* **Error Tracking:** Integration ready for Sentry to capture unhandled client/server runtime exceptions.

---

## 5. Security Verification & Test Log

All controls were tested with [`server/test_security.py`](file:///Users/pratish/Desktop/Sevenseas%20Broadband/server/test_security.py):

| Test Case | Attack / Probe Vector | Result | Status |
| :--- | :--- | :--- | :--- |
| **SQL Injection** | `' OR '1'='1`, `'; DROP TABLE leads; --`, `1' UNION SELECT...` | Parameterized literally; table remains intact | **PASSED** |
| **Email Header Injection** | `\r\nBcc: attacker@spam.com` injected into name field | CRLF stripped before header construction | **PASSED** |
| **XSS Escaping** | `<script>alert("XSS")</script>` | Sanitized to `&lt;script&gt;...` | **PASSED** |
| **Honeypot Bot** | Form posted with non-empty `b_website` | Flagged as automated bot and rejected | **PASSED** |
| **Mobile Regex** | Non-Indian numbers (`0123...`, `5123...`, short/long) | Rejected with explicit error message | **PASSED** |
| **Rate Limiter** | 6 consecutive requests within window | Request 6 rejected with HTTP 429 | **PASSED** |
| **Security Headers** | Inspection of HSTS, CSP, X-Frame-Options | All 6 standard security headers present | **PASSED** |

---

## 6. Honest Security Disclaimer
Security is an ongoing operational process, not an absolute state. While the controls documented above adhere to telecom best practices and current OWASP recommendations, no website can be claimed to be completely impenetrable. Routine penetration testing, dependency patching (`npm audit`), and administrative credential hygiene remain essential.
