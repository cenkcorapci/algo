# algo

[![Build](https://github.com/cenkcorapci/algo/actions/workflows/build.yml/badge.svg)](https://github.com/cenkcorapci/algo/actions/workflows/build.yml)
[![Test](https://github.com/cenkcorapci/algo/actions/workflows/test.yml/badge.svg)](https://github.com/cenkcorapci/algo/actions/workflows/test.yml)
[![Coverage](https://codecov.io/gh/cenkcorapci/algo/graph/badge.svg)](https://codecov.io/gh/cenkcorapci/algo)

Algorithms workspace powered by Bazel for `cpp`, `go`, `python`, `scala`, `rust`, and `javascript`.

This repo follows a consistent question layout:

```text
/{hackerrank,leetcode,other}/{collection}/{question}/{python,go,cpp,scala,rust,js}
```

Example:

```text
leetcode/arrays/two_sum/python
leetcode/arrays/two_sum/go
leetcode/arrays/two_sum/cpp
leetcode/arrays/two_sum/scala
leetcode/arrays/two_sum/rust
leetcode/arrays/two_sum/js
```

## Tooling

- Bazel + bzlmod (`MODULE.bazel`) for multi-language builds/tests.
- Make targets for running/testing one question or all tests.
- Per-question Bazel target convention:
  - `:run` for execution
  - `:test` for unit tests

Requires `bazel` (or `bazelisk`) and `python3` on your `PATH`. JavaScript targets also need `node`.

## Make commands

Create a new question from the platform templates (copies every available language unless `LANGS` is set):

```bash
make new DIR=leetcode/arrays NAME=product_except_self
make new DIR=hackerrank/warmup NAME=simple_array_sum LANGS="python go"
```

`DIR` is `<platform>/<collection>` (`leetcode`, `hackerrank`, or `other`). `NAME` is the snake_case question slug. This also writes a stub `README.md` under the new question folder.

Run one solution (language + question only):

```bash
make run LANG=python QUESTION=two_sum
```

Test one solution:

```bash
make test LANG=go QUESTION=two_sum
```

Supported `LANG` values: `python`, `go`, `cpp`, `scala`, `rust`, `javascript` (alias: `js`).

If question names clash, disambiguate with full path form:

```bash
make test LANG=cpp QUESTION=leetcode/arrays/two_sum
```

Show available targets:

```bash
make help
```

Test everything:

```bash
make test-all
```

## CI/CD

GitHub Actions workflows under `.github/workflows/`:

| Workflow | What it runs |
| --- | --- |
| `build.yml` | `bazelisk build //...` |
| `test.yml` | `bazelisk test //...` |
| `coverage.yml` | `bazelisk coverage //...` and uploads LCOV to Codecov |

Every question package with a `BUILD.bazel` is included automatically; no path filters.

## Templates

Template question skeletons exist in each platform and language:

- `leetcode/templates/lc_template_question/{python,go,cpp,scala,rust,js}`
- `hackerrank/templates/hr_template_question/{python,go,cpp}`
- `other/templates/other_template_question/{python,go,cpp}`

Prefer `make new` over copying by hand — it rewrites Go `importpath`, Rust crate names, and C++ include guards for the new path.

## Questions

Sample multi-language question:

- `leetcode/arrays/two_sum/{python,go,cpp,scala,rust,js}`

Migrated Blind 75 solutions (each language has `solution.*`, tests, and `BUILD.bazel` with `:run` / `:test`):

- `leetcode/stacks/valid_parentheses/{python,go,cpp,scala,rust,js}`
- `leetcode/linked_lists/merge_two_sorted_lists/{python,go,cpp,scala,rust,js}`
- `leetcode/bit_manipulation/reverse_bits/{python,go,cpp,scala,rust,js}`
- `leetcode/dynamic_programming/combination_sum4/{python,go,cpp,scala,rust,js}`

Also present:

- `leetcode/strings/palindromic_substrings/{cpp,rust}`
