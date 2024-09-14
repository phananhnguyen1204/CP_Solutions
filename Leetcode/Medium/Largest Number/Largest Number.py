class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numStr = [str(num) for num in nums]
        def compare(a, b):
            return 1 if (a + b) < (b + a) else -1
        
        numStr.sort(key = cmp_to_key(compare))
        if numStr[0] == "0": return "0"
        return "".join(numStr)