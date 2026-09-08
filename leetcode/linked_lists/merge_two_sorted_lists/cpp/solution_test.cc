#include <cassert>
#include <initializer_list>
#include <vector>

#include "solution.h"

namespace {

ListNode* BuildList(std::initializer_list<int> values) {
    ListNode* head = nullptr;
    ListNode* tail = nullptr;
    for (int value : values) {
        ListNode* node = new ListNode(value);
        if (head == nullptr) {
            head = node;
            tail = node;
        } else {
            tail->next = node;
            tail = node;
        }
    }
    return head;
}

std::vector<int> ToVector(ListNode* head) {
    std::vector<int> values;
    while (head != nullptr) {
        values.push_back(head->val);
        head = head->next;
    }
    return values;
}

}  // namespace

int main() {
    Solution solution;

    {
        ListNode* list1 = BuildList({1, 2, 4});
        ListNode* list2 = BuildList({1, 3, 4});
        auto* merged = solution.mergeTwoLists(list1, list2);
        assert((ToVector(merged) == std::vector<int>{1, 1, 2, 3, 4, 4}));
    }

    {
        ListNode* list1 = nullptr;
        ListNode* list2 = BuildList({0});
        auto* merged = solution.mergeTwoLists(list1, list2);
        assert((ToVector(merged) == std::vector<int>{0}));
    }

    {
        ListNode* list1 = BuildList({1, 2, 3});
        ListNode* list2 = nullptr;
        auto* merged = solution.mergeTwoLists(list1, list2);
        assert((ToVector(merged) == std::vector<int>{1, 2, 3}));
    }

    return 0;
}
