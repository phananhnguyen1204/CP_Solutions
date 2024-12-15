from heapq import heappush, heappop
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)

        def pass_ratio_gain(num_pass, num_students):
            return (num_pass + 1) / (num_students + 1) - (num_pass / num_students)


        max_gains = []
        for passi, totali in classes:
            gains = pass_ratio_gain(passi, totali)
            heappush(max_gains, (-gains, passi, totali))

        for _ in range(extraStudents):
            gains, passi, totali = heappop(max_gains)
            gains += -1
            
            new_gains = pass_ratio_gain(passi+1, totali+1)
            heappush(max_gains, (-new_gains, passi+1, totali+1))

        pass_ratio = 0
        while max_gains:
            _, passi, totali = heappop(max_gains)
            pass_ratio += (passi / totali)

        return pass_ratio / n
            

