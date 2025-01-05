class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1

        one, two, three = 1, 1, 0
        for i in range(3, n + 1):
            temp1 = one
            temp2 = two

            one = one + two + three
            two = temp1
            three = temp2
        
        return one