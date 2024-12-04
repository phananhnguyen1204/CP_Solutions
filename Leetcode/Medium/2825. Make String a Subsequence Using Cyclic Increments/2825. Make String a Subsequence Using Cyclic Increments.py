class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0

        for i in range(len(str1)):
            if j == len(str2): return True
            
            if str1[i] == str2[j]:
                j += 1
            else:
                if ord(str2[j]) == ord(str1[i]) + 1 or ord(str2[j]) + 25 == ord(str1[i]):
                    j += 1

        return j == len(str2)