# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, t, s):
            if not root:
                return False
            
            c = root.val + s

            if (
                c == targetSum and
                not root.left and
                not root.right
            ):
                return True
            
            return dfs(root.left, t, c) or dfs(root.right, t, c)
        
        return dfs(root, targetSum, 0)
