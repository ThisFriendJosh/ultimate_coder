#!/usr/bin/env python3
"""CLI for Ultimate Coder knowledgebase."""

from __future__ import annotations

import argparse
import sys
import webbrowser
from pathlib import Path

# Path to knowledgebase
KB_PATH = Path(__file__).resolve().parents[1] / "ultimate_coder" / "resources" / "knowledgebase.yaml"


def load_kb() -> dict:
    """Load the knowledgebase YAML file without external deps."""
    if not KB_PATH.exists():
        raise FileNotFoundError(f"Knowledgebase not found at {KB_PATH}")

    kb: dict[str, dict[str, str]] = {}
    current: str | None = None
    with KB_PATH.open() as fh:
        for line in fh:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if not line.startswith(" "):
                current = line.strip().rstrip(":")
                kb[current] = {}
            elif current and ":" in line:
                key, value = line.split(":", 1)
                kb[current][key.strip()] = value.strip()
    return kb


def list_entries(kb: dict) -> None:
    for key, info in kb.items():
        desc = info.get("description", "")
        url = info.get("url", "")
        print(f"{key}: {desc} ({url})")


def search_entries(kb: dict, term: str) -> None:
    term_lower = term.lower()
    for key, info in kb.items():
        haystack = f"{key} {info.get('description', '')} {info.get('url', '')}".lower()
        if term_lower in haystack:
            desc = info.get("description", "")
            url = info.get("url", "")
            print(f"{key}: {desc} ({url})")


def open_entry(kb: dict, key: str) -> int:
    info = kb.get(key)
    if not info:
        print(f"{key} not found")
        return 1
    url = info.get("url")
    if not url:
        print(f"No URL for {key}")
        return 1
    webbrowser.open(url)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Lookup resources in the Ultimate Coder knowledgebase")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="show all entries")

    p_search = sub.add_parser("search", help="search entries")
    p_search.add_argument("term")

    p_open = sub.add_parser("open", help="open entry URL")
    p_open.add_argument("key")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    kb = load_kb()

    if args.command == "list":
        list_entries(kb)
        return 0
    if args.command == "search":
        search_entries(kb, args.term)
        return 0
    if args.command == "open":
        return open_entry(kb, args.key)
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
