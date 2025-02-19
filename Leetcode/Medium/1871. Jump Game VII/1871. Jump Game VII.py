class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        binary string
        """
        q= deque()
        n = len(s)
        q.append(0)
        farthest = 0

        while q:
            i = q.popleft()
            start = max(i + minJump, farthest + 1)
            # next candidate
            for j in range(start, min(i + maxJump + 1, n)):
                if s[j] == '0':
                    if j == n - 1: return True
                    q.append(j)
            farthest = i + maxJump
        return False
                
        