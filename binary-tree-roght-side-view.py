# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            lvl = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    lvl.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if lvl:
                res.append(lvl[-1])

        return res
