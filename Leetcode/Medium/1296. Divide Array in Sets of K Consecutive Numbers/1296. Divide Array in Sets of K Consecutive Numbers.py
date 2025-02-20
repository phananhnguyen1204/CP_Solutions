class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        nums.sort()
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for num in nums:
            if freq[num] > 0:
                for j in range(k):
                    if freq[num + j] == 0:
                        return False
                    freq[num + j] -= 1
        return True