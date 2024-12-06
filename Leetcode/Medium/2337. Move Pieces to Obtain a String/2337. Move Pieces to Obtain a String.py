class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """
        L___R

        """
        n1, n2 = len(start), leån(target)
        i, j = 0, 0
        while i < n1 or j < n2:
            while i < n1 and start[i] == '_':
                i += 1
            while j < n2 and target[j] == '_':
                j += 1
            if j == n2 or i == n1:
                break
            if start[i] == target[j]:
                if start[i] == 'L' and i < j: return False
                if start[i] == 'R' and i > j: return False
            else:
                return False
            i += 1
            j += 1
        
        return i == n1 and j == n2