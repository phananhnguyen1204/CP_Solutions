class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freqs1, freqs2 = {}, {}

        for num in nums1:
            freqs1[num] = freqs1.get(num, 0) + 1
        
        for num in nums2:
            freqs2[num] = freqs2.get(num, 0) + 1

        res = []
        for num, cnt in freqs1.items():
            if num in freqs2:
                for i in range(min(cnt, freqs2[num])):
                    res.append(num)

        return res