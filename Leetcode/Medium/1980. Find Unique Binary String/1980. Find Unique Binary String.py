class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Important: every string has lenght n
        """
        n = len(nums)
        res = [""] * n
        for i in range(n):
            if nums[i][i] == "0":
                res[i] = "1"
            else:
                res[i] = "0"
        return "".join(res)

