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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int len = 0;

        ListNode *p = head;
        while (p) {
            len++;
            p = p->next;
        }

        int remove = len - n;

        if (remove == 0) {
            ListNode* newHead = head->next;
            delete head;
            return newHead;
        }

        ListNode* current = head;
        ListNode* temp;

        while (remove-- > 0) {
            temp = current;
            current = current->next;

        }

        temp->next = current->next;
        delete current;

        return head;
    }
};
