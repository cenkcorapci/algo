package main

import "fmt"

func Solve(nums []int, target int) int {
	dp := make([]int, target+1)
	dp[0] = 1
	for i := 1; i <= target; i++ {
		for _, num := range nums {
			if i-num >= 0 {
				dp[i] += dp[i-num]
			}
		}
	}
	return dp[target]
}

func main() {
	fmt.Println(Solve([]int{1, 2, 3}, 4))
}
