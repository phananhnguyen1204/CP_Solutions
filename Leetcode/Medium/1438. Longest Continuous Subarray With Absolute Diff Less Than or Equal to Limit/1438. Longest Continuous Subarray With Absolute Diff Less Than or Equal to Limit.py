class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        need to find max(subarray) - min(subarray) <= limit
        if to find max(subarray) - min(subarray) > limit -> can not include any more element because it will creat
                                                        -> new min or new max -> increase the difference
        -> shrink the window
        -> sliding window use 2 monotonic deque
        -> maxD: decreasing monotonic deque
        -> minD: increasing monotonic deque

        maxD = [2]
        minD = [2]
        """

        maxD = deque()
        minD = deque()
        res = l = 0
        n = len(nums)

        for r in range(n):
            while maxD and nums[maxD[-1]] < nums[r]:
                maxD.pop()
            while minD and nums[minD[-1]] > nums[r]:
                minD.pop()

            maxD.append(r)
            minD.append(r)

            while nums[maxD[0]] - nums[minD[0]] > limit:
                l += 1
                if l > maxD[0]: maxD.popleft()
                if l > minD[0]: minD.popleft()
            
            res = max(res, r - l + 1)

        return res
            