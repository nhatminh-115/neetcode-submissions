"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        OldtoNew = {}

        def dfs(node):
            if node in OldtoNew:
                return OldtoNew[node] #tránh dup, kiểu nhiều node cùng tới 1 node.
            
            copy = Node(node.val)
            OldtoNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        if not node:
            return None
        
        return dfs(node)