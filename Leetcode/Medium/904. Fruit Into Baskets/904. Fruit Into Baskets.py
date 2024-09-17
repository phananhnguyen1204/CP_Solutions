class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        l = 0
        res = 0
        for r in range(len(fruits)):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1 
            if len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0: del basket[fruits[l]]
                l += 1
            res = max(r - l + 1, res)
        return res