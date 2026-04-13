package main

import (
	"fmt"
	"io"
	"os"
	"strings"
)

func Solve(input string) string {
	return strings.TrimSpace(input)
}

func main() {
	data, err := io.ReadAll(os.Stdin)
	if err != nil {
		panic(err)
	}
	fmt.Println(Solve(string(data)))
}

