# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(curr):
            if not curr:
                return (True, 0)
            
            lBalanced, lHeight = dfs(curr.left)
            rBalanced, rHeight = dfs(curr.right)

            balanced = ((lBalanced and rBalanced) and abs(lHeight - rHeight) <= 1)
            height = max(lHeight, rHeight)

            if not (lBalanced and rBalanced):
                return (False, height)

            return (balanced, height + 1)
        
        return dfs(root)[0]
