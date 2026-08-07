# Apify Local Setup

Use this optional integration for public-source discovery only. It does not use browser cookies and must not be used to fetch LinkedIn post bodies.

## One-time local setup

1. Create an Apify account and create a token in Apify Console: **Settings → API & Integrations**.
2. In the repository root, copy `.env.example` to `.env`, then set `APIFY_TOKEN` to the token. Keep `.env` local.
3. Optionally create a local Python environment (the runner uses only the Python standard library):

   ```powershell
   python -m venv .venv
   ```

## Run a small discovery test

Create a local input file such as `tasks\demo\google-search.json`:

```json
{
  "queries": "site:linkedin.com/posts PwC UK Audit interview experience",
  "maxPagesPerQuery": 1
}
```

Then run:

```powershell
python scripts\run_apify_actor.py `
  --actor apify/google-search-scraper `
  --input tasks\demo\google-search.json `
  --output tasks\demo\api\google-search-results.json
```

Treat a LinkedIn result only as a candidate URL. Record it in the platform log, then manually inspect the visible post in the user's logged-in browser. Do not treat search snippets as interview evidence.

## Public-page crawler

Use `apify/website-content-crawler` only after confirming that the exact URL is public and readable without bypassing a restriction. The runner rejects LinkedIn URLs. Limit the first run to a small URL set and save output under `tasks/`, which is excluded from Git.

## Team sharing

Commit only this guide, the runner, and `.env.example`. Do not commit `.env`, API responses, screenshots, cookies, or task evidence. Each teammate creates their own token and local `.env`.
