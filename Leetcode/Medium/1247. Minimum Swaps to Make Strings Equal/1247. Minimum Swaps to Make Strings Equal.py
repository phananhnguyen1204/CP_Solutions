class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """
        xyx 
        yyy -> 1 swap -> prioritize swaping this way?
        only when # of pair (x_y or y_x) is even

        xy -> 2 swap -> have to do this when (x_y) and y_x is odd
        yx

        xy
        xx -> impossible

        cnt_diff % 2 == 1 -> impossible
        """

        cnt_xy = cnt_yx = 0
        n = len(s1)
        if s1 == s2: return 0
        res = 0

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x': cnt_xy += 1
                else: cnt_yx += 1
        if (cnt_xy + cnt_yx) % 2 == 1: return -1

        res += cnt_xy // 2 + cnt_yx // 2 + cnt_xy % 2 + cnt_yx % 2
        return res