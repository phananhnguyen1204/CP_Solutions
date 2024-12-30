"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        mapping = {}
        def dfs(root):
            if root not in mapping:
                mapping[root] = Node(root.val, [])
                for neighbor in root.neighbors:
                    mapping[root].neighbors.append(dfs(neighbor))

            return mapping[root]
        
        return dfs(node)
