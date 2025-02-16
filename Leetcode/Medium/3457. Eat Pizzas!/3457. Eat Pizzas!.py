class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        """
        to maximize the weight: 
        - on odd day: group of 4 = (maximum, 3th minimum)
        - on even day: group of 4 = (2 maximum, 2th minimum)
        always pick pizza for an odd day first (it's not optimal if we do alternatively)
        [5,2,2,4,3,3,1,3,2,5,4,2]
                           l           
        -> [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]
                                    r
        res = 13
        
        """
        res = 0
        day = 1
        n = len(pizzas)
        total_days = n // 4
        odd_days = (total_days + 1) // 2
        even_days = total_days - odd_days
        pizzas.sort()
        i = n - 1

        for day in range(odd_days):
            res += pizzas[i]
            i -= 1

        for day in range(even_days):
            i -= 1
            res += pizzas[i]
            i -= 1

        return res