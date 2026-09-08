#!/bin/sh
set -e
# Bazel sandboxes strip Homebrew from PATH; allow a local Node runtime.
export PATH="/opt/homebrew/bin:/usr/local/bin:${PATH}"
cd "$(dirname "$0")"
if ! command -v node >/dev/null 2>&1; then
  echo "node is required on PATH to run JavaScript solutions" >&2
  exit 127
fi
node ./test_solution.js
