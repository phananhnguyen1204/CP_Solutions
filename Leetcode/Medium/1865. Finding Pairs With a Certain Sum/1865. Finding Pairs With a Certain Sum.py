class FindSumPairs:
    # since len(nums1) < len(nums2) -> iterate nums1 instead of nums2
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        # num -> cnt
        self.freq = defaultdict(int)
        for num in nums2:
            self.freq[num] += 1
        

    def add(self, index: int, val: int) -> None:
        self.freq[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1 

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            if tot - num in self.freq:
                res += self.freq[tot - num]
        return res
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)