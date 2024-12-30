class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        m, n = len(image), len(image[0])
        

        def dfs(r, c, original_color):
            image[r][c] = color
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if nr >= 0 and nr < m and nc >= 0 and nc < n and image[nr][nc] == original_color:
                    dfs(nr, nc, original_color)
        
        dfs(sr, sc, image[sr][sc])
        return image

        