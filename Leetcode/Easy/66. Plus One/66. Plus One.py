class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = [0] * (n+1)
        carry = 1
        for i in range(n-1,-1,-1):
            new_digit = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            res[i+1] = new_digit
        
        if carry == 1:
            res[0] = 1
            return res
        return res[1:]
            
            