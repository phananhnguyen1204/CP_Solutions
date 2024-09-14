class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = float("inf")
        res = -1
        total = 0
        for customer in customers:
            if customer == 'Y':
                total += 1
        left = 0
        for i, customer in enumerate(customers):
            if penalty > total + left:
                penalty = total + left
                res = i
            if customer == 'N':
                left  += 1
            if customer == 'Y':
                total -= 1
        #Base case: 
        if penalty > total + left:
            res = i + 1
        return res
