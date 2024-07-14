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
    ListNode *modifiedList(vector<int> &nums, ListNode *head)
    {
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        unordered_set<int> seen;
        for (auto num : nums)
            seen.insert(num);
        ListNode *curr = dummy->next;
        ListNode *prev = dummy;
        ListNode *next = nullptr;
        while (curr != nullptr)
        {
            if (seen.find(curr->val) != seen.end())
            {
                next = curr->next;
                prev->next = next;
                curr = next;
            }
            else
            {
                prev = curr;
                curr = curr->next;
            }
        }
        return dummy->next;
    }
};