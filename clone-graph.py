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
        if not node:
            return None
        
        cloned = {}
        
        def dfs(original_node):
            if original_node.val in cloned:
                return cloned[original_node.val]
            
            # Create the clone first
            clone = Node(original_node.val)
            cloned[original_node.val] = clone
            
            # Then clone all neighbors and add them
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
