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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummy = new ListNode(0, head);

        ListNode* prevgroup = dummy;

        while (true) {
            ListNode* kth = getKth(prevgroup, k);
            if (!kth) {
                break;
            }

            ListNode* nextgroup = kth->next;
            ListNode* prev = kth->next;
            ListNode* cur = prevgroup->next;

            while (cur != nextgroup) {
                ListNode* temp = cur->next;
                cur->next = prev;
                prev = cur;
                cur = temp;
            }

            ListNode* temp = prevgroup->next;
            prevgroup->next = kth;
            prevgroup = temp;
            
        }

        return dummy->next;
    }


    ListNode* getKth(ListNode* curr, int k) {
        while (curr && k > 0) {
            curr = curr->next;
            k--;
        }
        return curr;
    }
};
