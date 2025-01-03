class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1, s2 = set(nums1), set(nums2)
        res = []

        for num in s1:
            if num in s2:
                res.append(num)

        return res
