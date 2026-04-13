package main

import "fmt"

func Solve(nums []int, target int) []int {
	seen := map[int]int{}
	for i, value := range nums {
		complement := target - value
		if j, ok := seen[complement]; ok {
			return []int{j, i}
		}
		seen[value] = i
	}
	return []int{}
}

func main() {
	fmt.Println(Solve([]int{2, 7, 11, 15}, 9))
}

