class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        sliding window not work since nums contains negative number
        prefix sum
        min_heap can help (prefix_sum, end idx)
        if our next prefix sum is greater than the one previously, we might remove all the previously -> since
        we want to minimize the size of subarray
        
        """
        n = len(nums)
        prefix = [0] * n
        minD = deque() # increasing monotonic deque
        res = float("inf")

        for i in range(n):
            prefix[i] = nums[i] if i == 0 else nums[i] + prefix[i - 1]

        for i in range(n):
            curr_sum = prefix[i]
            if curr_sum >= k:
                res = min(res, i + 1)

            while minD and curr_sum - prefix[minD[0]] >= k:
                res = min(res, i - minD[0])
                minD.popleft()
            
            while minD and prefix[minD[-1]] >= curr_sum:
                minD.pop()
            minD.append(i)

        return res if res != float("inf") else -1

        