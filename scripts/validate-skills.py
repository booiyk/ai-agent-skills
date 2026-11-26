#!/usr/bin/env python3
"""
Smoke test SKILL.md collection.

Memverifikasi setiap SKILL.md di skills/ memiliki frontmatter yang valid
mengandung kunci `name` dan `description`.
Stdlib saja, tidak butuh package tambahan.
"""
import os
import re
import sys

SKILLS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "skills")
REQUIRED = ("name", "description")


def find_skill_files(root):
    for dirpath, _dirnames, filenames in os.walk(root):
        if "SKILL.md" in filenames:
            yield os.path.join(dirpath, "SKILL.md")


def read_frontmatter(path):
    """Return (body, error). body is None when frontmatter is invalid."""
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    if not lines or lines[0] != "---":
        return None, "tidak memakai frontmatter (tidak diawali '---')"
    end = None
    for i in range(1, len(lines)):
        if lines[i] == "---":
            end = i
            break
    if end is None:
        return None, "frontmatter tidak ditutup ('---')"
    return "\n".join(lines[1:end]), None


def main():
    root = os.path.abspath(SKILLS_DIR)
    files = sorted(find_skill_files(root))
    if not files:
        print("Tidak ada SKILL.md ditemukan di", root)
        return 1

    failed = 0
    for path in files:
        rel = os.path.relpath(path, root)
        body, err = read_frontmatter(path)
        if err is not None:
            print(f"GAGAL  {rel}: {err}")
            failed += 1
            continue
        if body is None:
            print(f"GAGAL  {rel}: frontmatter hilang secara aneh")
            failed += 1
            continue
        missing = [k for k in REQUIRED if not re.search(rf"^{k}:", body, re.MULTILINE)]
        if missing:
            print(f"GAGAL  {rel}: missing keys {missing}")
            failed += 1
        else:
            print(f"OK      {rel}")

    print(f"\n{len(files) - failed}/{len(files)} skill valid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
