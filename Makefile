SHELL := /bin/sh
BAZEL := $(shell command -v bazel >/dev/null 2>&1 && echo bazel || (command -v bazelisk >/dev/null 2>&1 && echo bazelisk))

.PHONY: help run test test-all

guard-bazel:
	@test -n "$(BAZEL)" || (echo "Install bazel (or bazelisk) to run this project." && exit 1)


help:
	@echo "Usage:"
 	@echo "  make run LANG=<python|go|cpp|scala|rust|javascript> QUESTION=<question-or-platform/collection/question>"
 	@echo "  make test LANG=<python|go|cpp|scala|rust|javascript> QUESTION=<question-or-platform/collection/question>"
	@echo "  make test-all"

run: guard-bazel
	@test -n "$(LANG)" || (echo "LANG is required" && exit 1)
	@test -n "$(QUESTION)" || (echo "QUESTION is required" && exit 1)
	@$(BAZEL) run "$$(python3 tools/find_target.py --lang "$(LANG)" --question "$(QUESTION)" --kind run)"

test: guard-bazel
	@test -n "$(LANG)" || (echo "LANG is required" && exit 1)
	@test -n "$(QUESTION)" || (echo "QUESTION is required" && exit 1)
	@$(BAZEL) test "$$(python3 tools/find_target.py --lang "$(LANG)" --question "$(QUESTION)" --kind test)"

test-all: guard-bazel
	@$(BAZEL) test //...

