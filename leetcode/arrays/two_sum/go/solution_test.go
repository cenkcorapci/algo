package main

import (
	"reflect"
	"testing"
)

func TestSolveFindsPair(t *testing.T) {
	got := Solve([]int{2, 7, 11, 15}, 9)
	want := []int{0, 1}
	if !reflect.DeepEqual(got, want) {
		t.Fatalf("Solve() = %v, want %v", got, want)
	}
}

func TestSolveReturnsEmptyWhenMissing(t *testing.T) {
	got := Solve([]int{1, 2, 3}, 99)
	if len(got) != 0 {
		t.Fatalf("Solve() = %v, want empty result", got)
	}
}

