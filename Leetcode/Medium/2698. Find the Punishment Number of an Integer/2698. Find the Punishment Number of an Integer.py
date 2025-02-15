class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0

        def can_partition(str_num, target):
            if not str_num:
                return target == 0
            for i in range(len(str_num)):
                left = str_num[:i+1]
                right = str_num[i + 1:]
                if can_partition(right, target - int(left)):
                    return True
            return False

        for i in range(1, n + 1):
            num = i * i
            if can_partition(str(num), i):
                res += num
        return res