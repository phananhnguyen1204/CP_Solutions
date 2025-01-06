class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        diff = [0] * length

        for start, end, inc in updates:
            diff[start] += inc
            if end + 1 < length:
                diff[end + 1] -= inc

        for i in range(1, length):
            diff[i] += diff[i - 1]
        
        return diff