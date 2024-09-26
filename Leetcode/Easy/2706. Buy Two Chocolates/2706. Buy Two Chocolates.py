class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float("inf")
        for i in range(len(prices)):
            if min1 > prices[i]:
                min1 = prices[i]
            elif min2 > prices[i]:
                min2 = prices[i]
        leftOver = money - min1 - min2
        return money if leftOver < 0 else leftOver