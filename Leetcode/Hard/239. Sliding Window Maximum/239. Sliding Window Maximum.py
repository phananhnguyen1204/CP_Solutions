class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxD = deque()
        l = 0
        n = len(nums)
        res = []
        for r in range(n):
            while maxD and nums[maxD[-1]] <= nums[r]:
                maxD.pop()
            maxD.append(r)
            if r >= k-1:
                res.append(nums[maxD[0]])
                l += 1
                if maxD[0] < l: maxD.popleft()

        return res
