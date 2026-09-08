SHELL := /bin/sh
BAZEL := $(shell command -v bazel >/dev/null 2>&1 && echo bazel || (command -v bazelisk >/dev/null 2>&1 && echo bazelisk))

.PHONY: help run test test-all new

guard-bazel:
	@test -n "$(BAZEL)" || (echo "Install bazel (or bazelisk) to run this project." && exit 1)


help:
	@echo "Usage:"
	@echo "  make run LANG=<python|go|cpp|scala|rust|javascript> QUESTION=<question-or-platform/collection/question>"
	@echo "  make test LANG=<python|go|cpp|scala|rust|javascript> QUESTION=<question-or-platform/collection/question>"
	@echo "  make new DIR=<platform/collection> NAME=<question_slug> [LANGS=\"python go\"]"
	@echo "  make test-all"

run: guard-bazel
	@test -n "$(LANG)" || (echo "LANG is required" && exit 1)
	@test -n "$(QUESTION)" || (echo "QUESTION is required" && exit 1)
	@$(BAZEL) run "$$(python3 tools/find_target.py --lang "$(LANG)" --question "$(QUESTION)" --kind run)"

test: guard-bazel
	@test -n "$(LANG)" || (echo "LANG is required" && exit 1)
	@test -n "$(QUESTION)" || (echo "QUESTION is required" && exit 1)
	@$(BAZEL) test "$$(python3 tools/find_target.py --lang "$(LANG)" --question "$(QUESTION)" --kind test)"

# Scaffold template solutions under DIR/NAME from the matching platform templates.
# Example: make new DIR=leetcode/arrays NAME=product_except_self
# Optional: LANGS="python cpp" to copy only those languages.
new:
	@test -n "$(DIR)" || (echo "DIR is required, e.g. DIR=leetcode/arrays" && exit 1)
	@test -n "$(NAME)" || (echo "NAME is required, e.g. NAME=product_except_self" && exit 1)
	@if [ -n "$(LANGS)" ]; then \
		set -- $(LANGS); \
		args=""; \
		for lang in "$$@"; do args="$$args --lang $$lang"; done; \
		python3 tools/new_question.py --dir "$(DIR)" --name "$(NAME)" $$args; \
	else \
		python3 tools/new_question.py --dir "$(DIR)" --name "$(NAME)"; \
	fi

test-all: guard-bazel
	@$(BAZEL) test //...
