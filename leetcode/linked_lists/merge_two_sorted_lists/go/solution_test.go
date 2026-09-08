package main

import (
	"reflect"
	"testing"
)

func TestSolve(t *testing.T) {
	cases := []struct {
		a, b, want []int
	}{
		{[]int{1, 2, 4}, []int{1, 3, 4}, []int{1, 1, 2, 3, 4, 4}},
		{nil, []int{0}, []int{0}},
		{[]int{1, 2, 3}, nil, []int{1, 2, 3}},
	}
	for _, tc := range cases {
		got := Solve(tc.a, tc.b)
		if !reflect.DeepEqual(got, tc.want) {
			t.Fatalf("Solve(%v, %v) = %v, want %v", tc.a, tc.b, got, tc.want)
		}
	}
}
