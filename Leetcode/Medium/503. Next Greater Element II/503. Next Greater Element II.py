class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        monotonic decreasing stack
        """
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
            print(stack)
        return res