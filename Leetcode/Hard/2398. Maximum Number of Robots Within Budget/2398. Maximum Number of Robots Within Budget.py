class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        """
        k consecutive -> if we run out of budget -> we can not run another robot
        -> can not expend the window -> need to shrink it -> sliding window
        """
        res = 0
        maxD = deque() # decreasing monotonic queue
        cost = l = 0
        n = len(chargeTimes)
        
        for r in range(n):
            cost += runningCosts[r]
            while maxD and chargeTimes[maxD[-1]] < chargeTimes[r]:
                maxD.pop()

            maxD.append(r)
            while maxD and cost * (r - l + 1) + chargeTimes[maxD[0]] > budget:
                cost -= runningCosts[l]
                l += 1
                if maxD[0] < l: maxD.popleft()
            res = max(r - l + 1, res)

        return res
                    