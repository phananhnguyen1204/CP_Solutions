class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        12
        34
        ---
        48
       360
          
        """
        if num1 == "0" or num2 == "0": return "0"
        n1 = len(num1)
        n2 = len(num2)
        pos = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2-1, -1, -1):
                val = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                sum_carry = val + pos[p2]
                pos[p2] = sum_carry % 10
                pos[p1] += sum_carry // 10
        
        res = ""
        for x in pos:
            res += str(x)
        return res.lstrip('0')