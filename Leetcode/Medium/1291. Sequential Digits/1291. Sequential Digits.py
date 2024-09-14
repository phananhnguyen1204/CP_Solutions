class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        sample = "123456789"
        for length in range(len(str(low)), len(str(high)) + 1):
            for i in range(9 - length + 1):
                num = int(sample[i : i + length])
                if low <= num <= high:
                    res.append(num)
        return res

