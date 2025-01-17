class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic increasing stack
        # area between 2 heights is defined by the smaller height
        stack = [] # (start_idx, height)
        n = len(heights)
        res = 0

        for i in range(n):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                # calculate the rectangle that has been covered by stack[-1][1]
                res = max(height * (i - idx), res)
                start = idx
            stack.append((start, heights[i]))

        for idx, height in stack:
            res = max(res, (n - idx) * height)
        return res
