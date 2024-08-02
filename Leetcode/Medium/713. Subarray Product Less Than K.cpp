class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int product = 1;
        int start = 0;
        int res = 0;
        for(int end = 0; end < nums.size(); end++){
            product *= nums[end];
            while(product >= k && start <= end){
                product /= nums[start];
                start++;
            }
            res += (end - start + 1);
        }
        return res;
    }
};