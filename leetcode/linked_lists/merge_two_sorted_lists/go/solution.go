package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1, list2 *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			tail.Next = list1
			list1 = list1.Next
		} else {
			tail.Next = list2
			list2 = list2.Next
		}
		tail = tail.Next
	}
	if list1 != nil {
		tail.Next = list1
	} else {
		tail.Next = list2
	}
	return dummy.Next
}

func buildList(values []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, value := range values {
		tail.Next = &ListNode{Val: value}
		tail = tail.Next
	}
	return dummy.Next
}

func toSlice(head *ListNode) []int {
	values := []int{}
	for head != nil {
		values = append(values, head.Val)
		head = head.Next
	}
	return values
}

func Solve(list1, list2 []int) []int {
	return toSlice(mergeTwoLists(buildList(list1), buildList(list2)))
}

func main() {
	fmt.Println(Solve([]int{1, 2, 4}, []int{1, 3, 4}))
}
