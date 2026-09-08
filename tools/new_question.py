#!/usr/bin/env python3
"""Scaffold a new question from platform templates."""

from __future__ import annotations

import argparse
import re
import shutil
import stat
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PLATFORMS = {
    "leetcode": "leetcode/templates/lc_template_question",
    "hackerrank": "hackerrank/templates/hr_template_question",
    "other": "other/templates/other_template_question",
}

SLUG_RE = re.compile(r"^[a-z][a-z0-9_]*$")
TEXT_SUFFIXES = {".bazel", ".bzl", ".h", ".cc", ".go", ".rs", ".scala", ".py", ".js", ".sh", ".md"}


def _die(message: str, code: int = 1) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)


def _title_case(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("_"))


def _cpp_guard(platform: str, collection: str, question: str) -> str:
    parts = [platform, collection, question, "cpp", "solution", "h"]
    return "_".join(p.upper() for p in parts) + "_"


def _rewrite_text(path: Path, replacements: list[tuple[str, str]]) -> None:
    text = path.read_text(encoding="utf-8")
    updated = text
    for old, new in replacements:
        updated = updated.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding="utf-8")


def _chmod_exec(path: Path) -> None:
    mode = path.stat().st_mode
    path.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def _write_readme(dest: Path, platform: str, collection: str, question: str, langs: list[str]) -> None:
    title = _title_case(question)
    lang_list = ", ".join(f"`{lang}`" for lang in langs)
    content = f"""# {title}

TODO: describe the problem.

## Approach

TODO: describe the solution approach and complexity.

## Languages

{lang_list} — each with `:run` and `:test`.

```bash
make test LANG={langs[0]} QUESTION={question}
make run LANG={langs[0]} QUESTION={question}
```

Full path (if the slug is ambiguous):

```bash
make test LANG={langs[0]} QUESTION={platform}/{collection}/{question}
```
"""
    (dest / "README.md").write_text(content, encoding="utf-8")


def scaffold(directory: str, name: str, langs: list[str] | None) -> Path:
    directory = directory.strip().strip("/")
    name = name.strip().strip("/")

    if not directory or not name:
        _die("DIR and NAME are required.")
    if not SLUG_RE.match(name):
        _die(f"NAME must be a snake_case slug matching {SLUG_RE.pattern}: got {name!r}")

    parts = Path(directory).parts
    if len(parts) != 2:
        _die(
            "DIR must be <platform>/<collection>, e.g. leetcode/arrays "
            f"(got {directory!r})."
        )

    platform, collection = parts
    if platform not in PLATFORMS:
        _die(f"Unknown platform {platform!r}. Expected one of: {', '.join(PLATFORMS)}.")
    if not SLUG_RE.match(collection):
        _die(f"collection must be snake_case: got {collection!r}")

    template_root = ROOT / PLATFORMS[platform]
    if not template_root.is_dir():
        _die(f"Template missing: {template_root.relative_to(ROOT)}")

    available = sorted(
        p.name for p in template_root.iterdir() if p.is_dir() and not p.name.startswith(".")
    )
    if not available:
        _die(f"No language templates under {template_root.relative_to(ROOT)}")

    if langs:
        unknown = [lang for lang in langs if lang not in available]
        if unknown:
            _die(
                f"Languages not in {platform} template: {', '.join(unknown)}. "
                f"Available: {', '.join(available)}"
            )
        selected = langs
    else:
        selected = available

    dest = ROOT / platform / collection / name
    if dest.exists():
        _die(f"Destination already exists: {dest.relative_to(ROOT)}")

    dest.mkdir(parents=True, exist_ok=False)

    template_rel = PLATFORMS[platform]
    dest_rel = f"{platform}/{collection}/{name}"

    template_guard = None
    template_header = template_root / "cpp" / "solution.h"
    if template_header.exists():
        match = re.search(r"#ifndef\s+(\w+)", template_header.read_text(encoding="utf-8"))
        if match:
            template_guard = match.group(1)
    new_guard = _cpp_guard(platform, collection, name)

    for lang in selected:
        src_lang = template_root / lang
        dst_lang = dest / lang
        shutil.copytree(src_lang, dst_lang)

        for script in list(dst_lang.glob("solution.js")) + list(dst_lang.glob("*.sh")):
            _chmod_exec(script)

        for path in dst_lang.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix not in TEXT_SUFFIXES and path.name not in {"BUILD.bazel", "lib.rs", "main.rs"}:
                continue

            replacements: list[tuple[str, str]] = [
                (f"algo/{template_rel}/{lang}", f"algo/{dest_rel}/{lang}"),
                (template_rel, dest_rel),
            ]
            if template_guard:
                replacements.append((template_guard, new_guard))

            if lang == "rust":
                replacements.extend(
                    [
                        ('name = "algo_templates"', f'name = "{name}"'),
                        (":algo_templates", f":{name}"),
                        ("algo_templates::", f"{name}::"),
                    ]
                )

            _rewrite_text(path, replacements)

    _write_readme(dest, platform, collection, name, selected)
    return dest.relative_to(ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new question from platform templates")
    parser.add_argument("--dir", required=True, help="Target collection directory: <platform>/<collection>")
    parser.add_argument("--name", required=True, help="Question slug (snake_case)")
    parser.add_argument(
        "--lang",
        action="append",
        dest="langs",
        help="Optional language to include (repeatable). Default: all template languages.",
    )
    args = parser.parse_args()

    rel = scaffold(args.dir, args.name, args.langs)
    print(f"Created {rel}")
    print("Next:")
    print(f"  make test LANG=python QUESTION={args.name}")
    print(f"  # or: make test LANG=python QUESTION={rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
