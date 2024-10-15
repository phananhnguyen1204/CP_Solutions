class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)
        self.sum = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.sum)
        
        l = 0
        r = len(self.prefix) - 1
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            if self.prefix[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()