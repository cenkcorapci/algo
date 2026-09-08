#include <iostream>

#include "solution.h"

ListNode* Solution::mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;

    while (list1 != nullptr && list2 != nullptr) {
        if (list1->val <= list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    tail->next = (list1 != nullptr) ? list1 : list2;
    return dummy.next;
}

#ifndef ALGO_TEST
int main() {
    ListNode* l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
    ListNode* l2 = new ListNode(1, new ListNode(3, new ListNode(4)));

    Solution solution;
    ListNode* merged = solution.mergeTwoLists(l1, l2);

    while (merged != nullptr) {
        std::cout << merged->val << " ";
        merged = merged->next;
    }
    std::cout << std::endl;
    return 0;
}
#endif
