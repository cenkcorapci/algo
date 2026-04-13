#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path

LANG_DIR = {
    "python": "python",
    "go": "go",
    "cpp": "cpp",
    "scala": "scala",
    "rust": "rust",
    "javascript": "js",
    "js": "js",
}


def _is_candidate(path: Path, question: str, lang_dir: str) -> bool:
    if path.name != lang_dir:
        return False
    if not (path / "BUILD.bazel").exists():
        return False
    parts = path.parts
    if len(parts) < 4:
        return False

    platform, collection, question_slug = parts[0], parts[1], parts[2]
    joined = f"{platform}/{collection}/{question_slug}"
    return question == question_slug or question == joined


def find_targets(question: str, lang: str, kind: str) -> list[str]:
    root = Path(__file__).resolve().parents[1]
    lang_dir = LANG_DIR[lang]
    matches: list[str] = []

    for platform in ("leetcode", "hackerrank", "other"):
        platform_root = root / platform
        if not platform_root.exists():
            continue

        for dirpath, dirnames, filenames in os.walk(platform_root):
            # Keep search focused on repo content, not editor/tooling folders.
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            path = Path(dirpath)
            if _is_candidate(path.relative_to(root), question, lang_dir):
                label = f"//{path.relative_to(root).as_posix()}:{kind}"
                matches.append(label)

    return sorted(matches)


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve Bazel run/test target for a question")
    parser.add_argument("--lang", required=True, choices=LANG_DIR.keys())
    parser.add_argument("--question", required=True)
    parser.add_argument("--kind", required=True, choices=("run", "test"))
    args = parser.parse_args()

    matches = find_targets(args.question.strip("/"), args.lang, args.kind)
    if not matches:
        print(
            f"No {args.lang} target found for question '{args.question}'. "
            "Use QUESTION=<slug> or QUESTION=<platform/collection/slug>.",
            file=sys.stderr,
        )
        return 1

    if len(matches) > 1:
        print(
            f"Multiple matches for '{args.question}' ({args.lang}):\n  " + "\n  ".join(matches),
            file=sys.stderr,
        )
        print("Use QUESTION=<platform/collection/slug> to disambiguate.", file=sys.stderr)
        return 2

    print(matches[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

