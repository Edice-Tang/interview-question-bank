#!/usr/bin/env python3
"""Run approved Apify Actors for public interview-source discovery only."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen


REPOSITORY = Path(__file__).resolve().parents[1]
ALLOWED_ACTORS = {
    "apify/google-search-scraper",
    "apify/website-content-crawler",
}


def contains_linkedin_url(value: Any) -> bool:
    """Return True only for an actual LinkedIn URL, not a search query string."""
    if isinstance(value, str):
        parsed = urlparse(value)
        host = parsed.hostname or ""
        return host == "linkedin.com" or host.endswith(".linkedin.com")
    if isinstance(value, list):
        return any(contains_linkedin_url(item) for item in value)
    if isinstance(value, dict):
        return any(contains_linkedin_url(item) for item in value.values())
    return False


def load_local_token() -> str | None:
    """Read APIFY_TOKEN from the local .env without requiring a third-party package."""
    env_path = REPOSITORY / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            key, separator, value = line.partition("=")
            if separator and key.strip() == "APIFY_TOKEN":
                return value.strip().strip('"').strip("'")
    return os.getenv("APIFY_TOKEN")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a limited Apify Actor for public-source discovery."
    )
    parser.add_argument("--actor", required=True, choices=sorted(ALLOWED_ACTORS))
    parser.add_argument("--input", required=True, type=Path, help="Path to an Actor input JSON file")
    parser.add_argument("--output", required=True, type=Path, help="Where to save the result JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        run_input = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read valid input JSON: {error}") from error
    if not isinstance(run_input, dict):
        raise SystemExit("Actor input must be a JSON object.")

    if args.actor == "apify/website-content-crawler" and contains_linkedin_url(run_input):
        raise SystemExit(
            "LinkedIn URLs are blocked: use Google Search only for discovery, then review visibly in the browser."
        )

    token = load_local_token()
    if not token:
        raise SystemExit("APIFY_TOKEN is missing. Add it to local .env; do not commit that file.")

    actor_name = args.actor.replace("/", "~", 1)
    endpoint = (
        "https://api.apify.com/v2/actors/"
        f"{quote(actor_name, safe='~')}/run-sync-get-dataset-items?token={quote(token, safe='')}"
    )
    request = Request(
        endpoint,
        data=json.dumps(run_input).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=300) as response:
            items = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        raise SystemExit(f"Apify request failed with HTTP {error.code}.") from error
    except URLError as error:
        raise SystemExit(f"Cannot reach Apify: {error.reason}") from error
    if not isinstance(items, list):
        raise SystemExit("Apify returned an unexpected result format.")
    output = {
        "actor": args.actor,
        "item_count": len(items),
        "items": items,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {len(items)} item(s) to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
