# Platform Routing and Access Boundaries

Use an external search engine to discover candidate pages, then read only pages available to the current browser session without bypassing restrictions.

| Platform | Preferred route | Stop / fallback rule |
|---|---|---|
| 一亩三分地 | External search → public post → human logged-in browser | Stop at additional permissions, points, paywall, or CAPTCHA |
| Glassdoor | Public company/interview page → logged-in browser if needed | Record actual role and location for every candidate record |
| LeetCode Discuss | External `site:` search → public post | Prefer technical roles; do not use unrelated role results |
| eFinancialCareers | External search → public article | Use for background only unless it contains traceable candidate experience |
| Blind | External search → human logged-in web/App review | Stop if no readable page is available; do not retry aggressive page loads |
| Reddit | Public search and reading; use official API only when authorized | Exclude private, deleted, or ambiguous posts |
| 小红书 | External discovery → human logged-in page/App | Use readable text only; exclude pure images or unreliable OCR |
| LinkedIn | Discovery only; human reviews a visible post manually | Do not automate content collection or treat snippets as evidence |
| InterviewDB | Public site/external search using company and role aliases | Do not declare `NO_HIT` until the required expansions are complete |

For every platform, distinguish “no candidate found” from “candidate found but body unreadable.”

