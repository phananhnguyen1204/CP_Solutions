class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        if rowIndex == 0:
            return [1]

        prev = [1]
        for row in range(rowIndex):
            prev = [0] + prev + [0]
            curr = []
            for i in range(len(prev) - 1):
                curr.append(prev[i] + prev[i + 1])
            prev = curr
        return prev
            
