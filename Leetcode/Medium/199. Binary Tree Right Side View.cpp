class Solution
{
public:
    vector<int> res;
    vector<int> rightSideView(TreeNode *root)
    {
        dfs(root, 0);
        return res;
    }

    void dfs(TreeNode *root, int level)
    {
        if (root == NULL)
        {
            return;
        }
        if (res.size() == level)
        {
            res.push_back(root->val);
        }
        dfs(root->right, level + 1);
        dfs(root->left, level + 1);
    }
};