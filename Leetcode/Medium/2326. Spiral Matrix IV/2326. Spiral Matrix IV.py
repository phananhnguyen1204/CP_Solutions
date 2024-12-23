# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        i = 0
        res = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        cur_node = head
        visited = set()
        r = c = 0

        if not cur_node: return res

        def valid(r, c):
            return r < m and r >= 0 and c < n and c >= 0 and (r, c) not in visited

        while i < m * n:
            if not cur_node:
                return res
            res[r][c] = cur_node.val
            cur_node = cur_node.next
            visited.add((r, c))
            i += 1

            dr, dc = dirs[dir_idx]
            if not valid(r + dr, c + dc):
                dir_idx = (dir_idx + 1) % 4

            dr, dc = dirs[dir_idx]
            r, c = r + dr, c + dc
        
        return res
                


            
        
        