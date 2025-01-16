class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        """
        decreasing monotonic stack
        You can see the right next greater element.
        Your left next greater element can see you.
        """

        n = len(heights)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            cnt = 1
            while stack and heights[stack[-1]] < heights[i]:
                res[i] += 1
                stack.pop()
            # i person can see another person who is taller than him or equal height on the right
            if stack:
                 res[i] += 1
            stack.append(i)
        return res