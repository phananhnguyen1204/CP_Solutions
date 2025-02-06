class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        """
        ever a * b = c * d -> we have 8 distinct pair in the form (a, b, c, d)
        2 * 2 * 2 = 8
        2 way to swap (a, b) and (c, d)
        2 ways to swap a and b
        2 ways to swap c and d
        """
        res = 0
        n = len(nums)
        freq_product = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                freq_product[nums[i] * nums[j]] += 1

        for freq in freq_product.values():
            pairs = freq * (freq - 1) // 2
            res += pairs * 8

        return res

        
