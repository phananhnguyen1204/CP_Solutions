class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == '+':
                tmp = 0
                tmp += scores[-1] + scores[-2]
                scores.append(tmp)
            elif op == 'D':
                tmp = scores[-1] * 2
                scores.append(tmp)
            elif op =='C':
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)