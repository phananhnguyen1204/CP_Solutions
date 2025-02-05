class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        """
        set: keep track of unique numbers in each word

        if size(set1) == size(set2): -> true
        if abs(size(set1) - size(set2)) >= 3 -> false 
        -> can not do this
        -> bruteforce?
        """

        freq1, freq2 = defaultdict(int), defaultdict(int)
        n1, n2 = len(word1), len(word2)

        for c in word1:
            freq1[c] += 1
        for c in word2:
            freq2[c] += 1

        def remove_and_insert(freq1, freq2, c1, c2):
            freq1[c1] -= 1
            freq1[c2] += 1

            if freq1[c1] == 0: del freq1[c1]

            freq2[c1] += 1
            freq2[c2] -= 1
            if freq2[c2] == 0: del freq2[c2]

        for i, cnt1 in freq1.items():
            for j, cnt2 in freq2.items():
                freq1_temp, freq2_temp = freq1.copy(), freq2.copy()
                remove_and_insert(freq1_temp, freq2_temp, i, j)               
                if len(freq1_temp) == len(freq2_temp):
                    return True
                # remove and add back will change the order of key 
        return False