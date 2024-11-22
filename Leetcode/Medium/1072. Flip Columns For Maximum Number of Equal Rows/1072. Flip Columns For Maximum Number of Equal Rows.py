class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freq_cnt = {}
        for curr_row in matrix:
            pattern = "".join("T" if curr_row[0] == num else "F" for num in curr_row )
            freq_cnt[pattern] = freq_cnt.get(pattern, 0) + 1
        
        return max(freq_cnt.values())