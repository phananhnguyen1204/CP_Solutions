class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # another approach is
        # using hashmap for each diagonal
        # since every diagonal r - c is unique -> can be used as a key
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]

        startRow = m - 1

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        # bottom-left triangle
        while startRow >= 0:
            temp = []

            r, c = startRow, 0
            while valid(r, c):
                print(r, c)
                temp.append(grid[r][c])
                r += 1
                c += 1
            temp.sort(reverse = True)

            r, c = startRow, 0
            for val in temp:
                res[r][c] = val
                r += 1
                c += 1
            startRow -= 1
        
        # top-right triangle
        startCol = n - 1
        while startCol > 0:
            temp = []

            r, c = 0, startCol
            while valid(r, c):
                temp.append(grid[r][c])
                r += 1
                c += 1
            temp.sort()
            r, c = 0, startCol
            for val in temp:
                res[r][c] = val
                r += 1
                c += 1

            startCol -= 1
        return res

