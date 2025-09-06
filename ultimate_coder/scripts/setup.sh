#!/usr/bin/env bash
set -euo pipefail

echo ">>> Ultimate Coder bootstrap"
echo "Date: $(date)"
echo

echo "[*] Recommended toolchain:"
echo "    - Python 3.13 (pkg at /mnt/data/python-3.13.7-macos11.pkg)"
echo "    - OpenJDK 26-ea (tar at /mnt/data/openjdk-26-ea+14_linux-x64_bin.tar.gz)"
echo "    - Notepad++ portable (zip at /mnt/data/npp.8.8.5.portable.x64.zip)"
echo "    - Ghidra (zip at /mnt/data/ghidra-master.zip)"
echo

python3 --version || true
java -version || true
echo
echo "Create a venv: python3 -m venv .venv && source .venv/bin/activate && python -m pip install -U pip"
echo "Happy building!"
