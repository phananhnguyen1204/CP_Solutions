class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_map = defaultdict(int)

        for x in nums1:
            for y in nums2:
                hash_map[x + y] += 1
        
        res = 0
        for x in nums3:
            for y in nums4:
                if (-x-y) in hash_map:
                    res += hash_map[-x-y]
        
        return res