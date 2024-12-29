class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapping = {}

        for i, word in enumerate(list1):
            mapping[word] = i
        
        res = []
        min_sum = 1e9
        for i in range(len(list2)):
            if list2[i] in mapping:
                if min_sum > i + mapping[list2[i]]:
                    min_sum = i + mapping[list2[i]]
                    res = [list2[i]]
                elif min_sum == i + mapping[list2[i]]:
                    res.append(list2[i])

        return res