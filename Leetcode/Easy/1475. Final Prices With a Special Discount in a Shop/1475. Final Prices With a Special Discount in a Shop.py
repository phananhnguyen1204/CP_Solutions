class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        res = [price for price in prices]

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                res[stack[-1]] -= price
                stack.pop()
            
            stack.append(i)

        return res