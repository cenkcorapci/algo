# algo

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

## Templates

Template question skeletons exist in each platform and language:

- `leetcode/templates/lc_template_question/{python,go,cpp,scala,rust,js}`
- `hackerrank/templates/hr_template_question/{python,go,cpp}`
- `other/templates/other_template_question/{python,go,cpp}`

Copy one of these directories to start a new question quickly.

## Current sample question

- `leetcode/arrays/two_sum/{python,go,cpp,scala,rust,js}`

Each language includes:

- `solution.*`
- language-specific unit test file
- `BUILD.bazel`

## Notes

- Existing legacy content under `blind-75/` is kept as-is and can be migrated gradually into the new structure.
