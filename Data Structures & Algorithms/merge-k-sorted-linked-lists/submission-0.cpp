/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;

        for (int i = 1; i < lists.size(); i++) {
            ListNode *l1 = lists[i];
            ListNode *l2 = lists[i - 1];

            lists[i] = merge(l1, l2);
        }

        return lists.back();
    }

    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;

        while (l1 && l2) {
            if (l1->val <= l2->val) {
                cur->next = l1;
                l1 = l1->next;
            } else {
                cur->next = l2;
                l2 = l2->next;
            }

            cur = cur->next;
        }

        if (l1) {
            cur->next = l1;
        } else cur->next = l2;

        return dummy->next;
    }
};
