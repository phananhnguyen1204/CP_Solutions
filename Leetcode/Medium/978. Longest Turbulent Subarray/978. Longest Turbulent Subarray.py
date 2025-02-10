class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        if n == 1: return 1

        # True: current ele greater than prev element
        # False: current ele less than prev element
        def sliding_window(initial_sign):
            sign = initial_sign
            max_len = 0
            l = 0

            for r in range(1, n):
                if sign:
                    if arr[r] <= arr[r - 1]:
                        l = r
                else:
                    if arr[r] >= arr[r - 1]:
                        l = r
                sign = not sign
                max_len = max(max_len, r - l + 1)
            return max_len

        return max(sliding_window(True), sliding_window(False))