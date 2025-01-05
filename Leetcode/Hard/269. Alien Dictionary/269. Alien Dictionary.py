class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(list)
        n = len(words)
        indegree = {}

        for word in words:
            for c in word:
                indegree[c] = 0

        for i in range(n - 1):
            word1, word2 = words[i], words[i + 1]
            if word1.find(word2) == 0 and len(word1) > len(word2):
                return ""
            for j in range(min(len(word1), len(word2))):
                c1, c2 = word1[j], word2[j]
                if c1 == c2:
                    continue
                if c1 != c2:
                    adj[c1].append(c2)
                    indegree[c2] += 1
                    break
        q = deque()

        for char, degree in indegree.items():
            if degree == 0:
                q.append(char)
        
        res = []
        while q:
            char = q.popleft()
            res.append(char)

            for next_char in adj[char]:
                indegree[next_char] -= 1
                if indegree[next_char] == 0:
                    q.append(next_char)

        return "".join(res) if len(res) == len(indegree) else ""
                

                
