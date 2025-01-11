class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
            
        parent = defaultdict(int)
        rank = defaultdict(int)
        unique_string = set()

        for word1, word2 in zip(sentence1, sentence2):
            unique_string.add(word1)
            unique_string.add(word2)

        for word1, word2 in similarPairs:
            unique_string.add(word1)
            unique_string.add(word2)

        for word in unique_string:
            rank[word] = 1
            parent[word] = word

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] >= rank[py]:
                parent[py] = px
                rank[px] += 1
            else:
                parent[px] = py
                rank[py] += 1

        for x, y in similarPairs:
            union(x, y)

        for i in range(len(sentence1)):
            c1, c2 = sentence1[i], sentence2[i]
            if find(c1) != find(c2):
                return False

        return True


        