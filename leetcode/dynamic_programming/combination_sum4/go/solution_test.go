package main

import "testing"

func TestSolve(t *testing.T) {
	if got := Solve([]int{1, 2, 3}, 4); got != 7 {
		t.Fatalf("Solve([1,2,3], 4) = %d, want 7", got)
	}
}
