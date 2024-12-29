class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            freqs = [0] * 26
            
            for c in string:
                freqs[ord(c) - ord('a')] += 1
            
            freqs = tuple(freqs)
            if freqs in anagrams:
                anagrams[freqs].append(string)
            else:
                anagrams[freqs] = [string]
        res = []
        for anagram in anagrams.values():
            res.append(anagram)

        return res
                
