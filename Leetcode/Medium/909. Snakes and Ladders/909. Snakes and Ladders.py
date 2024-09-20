class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        '''
            [-1,-1,19,10,-1],
            [2,-1,-1,6,-1],
            [-1,17,-1,19,-1],
            [25,-1,20,-1,-1],
            [-1,-1,-1,-1,15]]
        '''

        n = len(board)
        q = deque()
        visited = set()
        
        def getPosition(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            r = n - 1 - r
            return (r, c)
        q.append(1)
        visited.add(1)
        level = 0
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                for i in range(1, 7):
                    next_square = curr + i
                    print(next_square)
                    r, c = getPosition(next_square)
                    print(r, c)
                    if next_square > n * n:
                        break
                    if board[r][c] != -1:
                        next_square = board[r][c]
                    if next_square == n * n:
                        return level + 1
                    if next_square not in visited:
                        q.append(next_square)
                        visited.add(next_square)
            level += 1
        return -1


                    
        