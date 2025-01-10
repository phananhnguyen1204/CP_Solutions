class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        curr_sum 

        [4, 5, 0, -2, -3, 1]
        """

        count_subarray = 0
        n = len(nums)
        total = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1

        for num in nums:
            total += num
            remainder = total % k
            count_subarray += sum_freq[remainder]
            sum_freq[remainder] += 1

        return count_subarray

        

        