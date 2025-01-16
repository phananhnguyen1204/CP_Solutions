class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # stack: monotonic decreasing
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack