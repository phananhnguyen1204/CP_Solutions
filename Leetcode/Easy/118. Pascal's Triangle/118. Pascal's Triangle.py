class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        if numRows == 1: 
            return res

        prev = [[1]]
        for row in range(2, numRows + 1):
            tmp = [1]
            for i in range(len(res[-1]) - 1):
                j = i + 1
                tmp.append(prev[i] + prev[j])
            tmp.append(1)
            prev = tmp
            res.append(tmp)
        
        return res

