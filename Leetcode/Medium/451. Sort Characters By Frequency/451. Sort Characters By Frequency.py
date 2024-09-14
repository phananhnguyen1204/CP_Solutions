class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        sorted_list = sorted(freq.items(), key = lambda x : -x[1])
        return "".join(char * freq for char, freq in sorted_list)