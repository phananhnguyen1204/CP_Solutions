class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        deadends = set(deadends)
        visited = set()

        q.append("0000")
        visited.add("0000")
        if "0000" in deadends: return -1
        if "0000" == target: return 0
        res = 0
        while q:
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                for i in range(4):
                    digit = str((int(word[i]) + 1) % 10)
                    next_word = word[:i] + digit + word[i + 1:]
                    if next_word == target:
                        return res + 1
                    if next_word not in visited and next_word not in deadends:
                        visited.add(next_word)
                        q.append(next_word)
                    digit = str((int(word[i]) - 1) % 10)
                    next_word = word[:i] + digit + word[i + 1:]
                    if next_word == target:
                        return res + 1
                    if next_word not in visited and next_word not in deadends:
                        visited.add(next_word)
                        q.append(next_word)

            res += 1
        return -1 
                    