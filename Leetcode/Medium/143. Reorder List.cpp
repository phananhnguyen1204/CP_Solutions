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
class Solution
{
public:
    void reorderList(ListNode *head)
    {
        ListNode *prev = nullptr;
        ListNode *slow = head;
        ListNode *fast = head;
        while (fast != nullptr && fast->next != nullptr)
        {
            fast = fast->next->next;
            prev = slow;
            slow = slow->next;
        }
        // head has odd number of nodes
        if (fast != nullptr)
        {
            prev = slow;
            slow = slow->next;
        }
        prev->next = nullptr;
        prev = nullptr;
        ListNode *next = nullptr;
        while (slow)
        {
            next = slow->next;
            slow->next = prev;
            prev = slow;
            slow = next;
        }
        // Merge 2 lists
        ListNode *head1 = head;
        ListNode *head2 = prev;
        ListNode *dummy = new ListNode(0);
        ListNode *curr = dummy;
        int cnt = 0;
        while (head1 != nullptr || head2 != nullptr)
        {
            if (head1 == nullptr)
            {
                curr->next = head2;
                break;
            }
            if (head2 == nullptr)
            {
                curr->next = head1;
                break;
            }
            if (cnt % 2 == 0)
            {
                curr->next = head1;
                head1 = head1->next;
            }
            else
            {
                curr->next = head2;
                head2 = head2->next;
            }
            curr = curr->next;
            cnt++;
        }
        head = dummy->next;
    }
};