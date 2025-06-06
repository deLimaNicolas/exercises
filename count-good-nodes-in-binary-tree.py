# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(curr, lastMax):
            if not curr:
                return 0
            if curr.val >= lastMax:
                return dfs(curr.left, curr.val) + dfs(curr.right, curr.val) + 1
            else:
                return dfs(curr.left, lastMax) + dfs(curr.right, lastMax)
            
        return dfs(root, float("-inf"))
