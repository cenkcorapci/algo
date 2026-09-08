package main

import "testing"

func TestSolve(t *testing.T) {
	if got := Solve(43261596); got != 964176192 {
		t.Fatalf("Solve(43261596) = %d, want 964176192", got)
	}
}
