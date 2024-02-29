/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isEvenOddTree(TreeNode* root) {
        if(!root->left && !root->right) return root->val % 2 == 1;
        queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        while(!q.empty()){
            int n = q.size();
            int prev = level % 2 == 0 ? 0 : 1e9;
            for(int i = 0; i < n; i++){
                auto curr = q.front();
                q.pop();
                    if(level % 2 == 0){
                        if(prev >= curr->val || curr->val % 2 == 0) return false;
                    }
                    else{
                        if(prev <= curr->val || curr->val %2 == 1) return false;
                    }
                if(curr->left) q.push(curr->left);
                if(curr->right) q.push(curr->right);
                prev = curr->val;
            }
            level++;
        }
        return true;

    }
};