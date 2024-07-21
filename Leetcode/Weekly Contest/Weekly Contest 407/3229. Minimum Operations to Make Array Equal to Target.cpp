class Solution {
public:
    long long minimumOperations(vector<int>& nums, vector<int>& target) {
        long long res = 0;
        for(int i = 0; i < nums.size(); i++){
            nums[i] = target[i] - nums[i];
        }
        res = abs(nums[0]);
        for(int i = 1; i < nums.size(); i++){
            if((long long)nums[i-1] * nums[i] > 0){
                if(abs(nums[i]) > abs(nums[i-1])){
                    res += abs(nums[i]) - abs(nums[i-1]);
                }
            }
            else res += abs(nums[i]);

        }

        return res;

    }
};