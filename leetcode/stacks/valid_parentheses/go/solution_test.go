package main

import "testing"

func TestSolve(t *testing.T) {
	cases := []struct {
		in   string
		want bool
	}{
		{"()", true},
		{"()[]{}", true},
		{"(]", false},
		{"([)]", false},
		{"(", false},
	}
	for _, tc := range cases {
		if got := Solve(tc.in); got != tc.want {
			t.Fatalf("Solve(%q) = %v, want %v", tc.in, got, tc.want)
		}
	}
}
