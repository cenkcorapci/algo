package main

import "fmt"

func Solve(n uint32) uint32 {
	var result uint32
	for i := 0; i < 32; i++ {
		result = (result << 1) | (n & 1)
		n >>= 1
	}
	return result
}

func main() {
	fmt.Println(Solve(43261596))
}
