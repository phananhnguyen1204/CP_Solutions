class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        vowels = "aeuoi
        a -> e

        e -> a
        e - > i

        i not -> i

        o -> i
        o -> u

        u -> a


        a_count = u_count + i_count + e_count

        i_count = e_count + o_count

        u_count = o_count + i_count

        o_count = i_count

        """
        MOD = 10 ** 9 + 7
        if n == 1:
            return 5

        memo = {}

        def dfs(i, vowel):
            if i == n - 1:
                return 1

            if (i, vowel) in memo:
                return memo[(i, vowel)]

            """

        a_count = u_count + i_count + e_count
        i_count = e_count + o_count
        u_count = o_count + i_count
        o_count = i_count
        e_count = a_count + i_count
            """
            count = 0
            if vowel == 'a':
                count = dfs(i + 1, 'u') + dfs(i + 1, 'i') + dfs(i + 1, 'e') % MOD
            elif vowel =='i':
                count = dfs(i + 1, 'e') + dfs(i + 1, 'o') % MOD
            elif vowel == 'u':
                count = dfs(i + 1, 'o') + dfs(i + 1, 'i') % MOD
            elif vowel == 'e':
                count = dfs(i + 1, 'a') + dfs(i + 1, 'i') % MOD
            else:
                count = dfs(i + 1, 'i') % MOD

            memo[(i, vowel)] = count
            return memo[(i, vowel)]

        return sum([dfs(0, vowel) for vowel in "aeoui"]) % MOD
