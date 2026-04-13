package main

import "testing"

func TestSolve(t *testing.T) {
	got := Solve("  abc  \n")
	if got != "abc" {
		t.Fatalf("Solve() = %q, want %q", got, "abc")
	}
}

