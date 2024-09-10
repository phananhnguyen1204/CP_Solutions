class Solution:
    def minSwaps(self, s: str) -> int:
        '''
        ]][[
        '''
        close = 0
        max_close = 0
        for c in s:
            if c == '[': close -= 1
            else: close += 1
            max_close = max(close, max_close)
        return (max_close + 1) // 2
