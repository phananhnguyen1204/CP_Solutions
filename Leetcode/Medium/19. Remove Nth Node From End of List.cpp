class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode *fast = head;
        while (n-- > 0)
        {
            fast = fast->next;
        }
        ListNode *prev = nullptr;
        ListNode *slow = head;
        while (fast != nullptr)
        {
            fast = fast->next;
            prev = slow;
            slow = slow->next;
        }
        if (prev != nullptr)
        {
            prev->next = slow->next;
        }
        else
        {
            head = slow->next;
        }
        return head;
    }
};