#!/usr/bin/env python3
"""
Health check for all YAML specs in the project.
- Validates syntax
- Detects duplicate keys
- Prints summary

Usage:
    python scripts/health_check.py
"""

import sys
from pathlib import Path
import yaml


class UniqueKeyLoader(yaml.SafeLoader):
    """Custom loader that errors on duplicate keys."""

    def construct_mapping(self, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in mapping:
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found duplicate key ({key})",
                    key_node.start_mark,
                )
            value = self.construct_object(value_node, deep=deep)
            mapping[key] = value
        return mapping


def check_yaml(path: Path) -> bool:
    try:
        with path.open("r", encoding="utf-8") as f:
            yaml.load(f, Loader=UniqueKeyLoader)
        print(f"✅ {path} is valid")
        return True
    except Exception as e:
        print(f"❌ {path} failed: {e}")
        return False


def main():
    root = Path(__file__).resolve().parents[1]
    yamls = list(root.rglob("*.yaml")) + list(root.rglob("*.yml")) + list(root.rglob("*.txt"))

    yamls = [p for p in yamls if "yaml" in p.suffix or p.name.endswith(".yaml") or p.name.endswith(".txt")]
    if not yamls:
        print("No YAML files found.")
        sys.exit(0)

    all_ok = True
    for y in yamls:
        ok = check_yaml(y)
        all_ok = all_ok and ok

    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
