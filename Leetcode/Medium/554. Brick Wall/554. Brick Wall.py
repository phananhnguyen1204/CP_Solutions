class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m = len(wall)
        cnt_gap = {}
        '''
        [1,2,2,1]
        [3,1,2]
        [1,3,2]
        [2.4]
        [3,1,2]
        [1,3,1,1]
        '''
        for row in wall:
            curr_sum = 0
            for i in range(len(row)-1):
                curr_sum += row[i]
                if curr_sum in cnt_gap:
                    cnt_gap[curr_sum] += 1
                else:
                    cnt_gap[curr_sum] = 1
        res = m
        for key,value in cnt_gap.items():
            res = min(res, m - value)
        return res

