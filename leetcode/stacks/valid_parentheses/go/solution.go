package main

import "fmt"

func Solve(s string) bool {
	open := make([]rune, 0, len(s))
	pairs := map[rune]rune{')': '(', ']': '[', '}': '{'}
	for _, c := range s {
		if c == '(' || c == '[' || c == '{' {
			open = append(open, c)
			continue
		}
		if len(open) == 0 || open[len(open)-1] != pairs[c] {
			return false
		}
		open = open[:len(open)-1]
	}
	return len(open) == 0
}

func main() {
	fmt.Println(Solve("()[]{}"))
}
