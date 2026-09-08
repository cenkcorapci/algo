#ifndef LEETCODE_LINKED_LISTS_MERGE_TWO_SORTED_LISTS_CPP_SOLUTION_H_
#define LEETCODE_LINKED_LISTS_MERGE_TWO_SORTED_LISTS_CPP_SOLUTION_H_

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* nextNode) : val(x), next(nextNode) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2);
};

#endif  // LEETCODE_LINKED_LISTS_MERGE_TWO_SORTED_LISTS_CPP_SOLUTION_H_
