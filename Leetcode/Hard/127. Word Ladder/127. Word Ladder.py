class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        hit -> *it, h*t, hi*
        """

        if endWord not in wordList:
            return 0

        q = deque()
        visited = set()
        combination_words = defaultdict(list)
        # conbination -> word
        # curr_word -> intermediate_word -> next_word
        
        for word in wordList:
            for i in range(len(word)):
                combination_word = word[:i] + "*" + word[i + 1:]
                combination_words[combination_word].append(word)

        q.append((beginWord, 1))
        visited.add(beginWord)
        while q:
            curr_word, time = q.popleft()
            visited.add(curr_word)
            if curr_word == endWord:
                return time
            for i in range(len(curr_word)):
                intermediate_word = curr_word[:i] + "*" + curr_word[i + 1:]
                for next_word in combination_words[intermediate_word]:
                    if next_word not in visited:
                        q.append((next_word, time + 1))

        return 0