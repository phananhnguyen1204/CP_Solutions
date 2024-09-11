class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = {}
        for (w, h) in rectangles:
            val = w / h
            cnt[val] = cnt.get(val,0) + 1
        res = 0
        for val in cnt.values():
            res += val * (val - 1) // 2
        return res
