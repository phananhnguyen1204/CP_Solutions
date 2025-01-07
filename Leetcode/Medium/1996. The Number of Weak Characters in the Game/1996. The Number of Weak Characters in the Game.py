class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (-x[0], x[1]))

        """
        [1, 2], [1, 3]
        """

        max_defence = 0
        cnt = 0

        for attack, defence in properties:
            if defence >= max_defence:
                max_defence = defence
            else:
                cnt += 1

        return cnt