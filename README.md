# algo

Algorithms workspace powered by Bazel for `cpp`, `go`, `python`, `scala`, and `rust`.

This repo now follows a consistent question layout:

```text
/{hackerrank,leetcode,other}/{collection}/{question}/{python,go,cpp}
```

Example:

```text
leetcode/arrays/two_sum/python
leetcode/arrays/two_sum/go
leetcode/arrays/two_sum/cpp
```

## Tooling

- Bazel + bzlmod (`MODULE.bazel`) for multi-language builds/tests.
- Make targets for running/testing one question or all tests.
- Per-question Bazel target convention:
  - `:run` for execution
  - `:test` for unit tests

## Make commands

Run one solution (language + question only):

```bash
make run LANG=python QUESTION=two_sum
```

Test one solution:

```bash
make test LANG=go QUESTION=two_sum
```

If question names clash, disambiguate with full path form:

```bash
make test LANG=cpp QUESTION=leetcode/arrays/two_sum
```

Test everything:

```bash
make test-all
```

## Templates

Template question skeletons exist in each platform and language:

- `leetcode/templates/lc_template_question/{python,go,cpp}`
- `hackerrank/templates/hr_template_question/{python,go,cpp}`
- `other/templates/other_template_question/{python,go,cpp}`

Copy one of these directories to start a new question quickly.

## Current sample question

- `leetcode/arrays/two_sum/{python,go,cpp}`

Each language includes:

- `solution.*`
- language-specific unit test file
- `BUILD.bazel`

## Notes

- Existing legacy content under `blind-75/` is kept as-is and can be migrated gradually into the new structure.
