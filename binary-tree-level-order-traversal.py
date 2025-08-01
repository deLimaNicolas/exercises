# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            qLen = len(queue)
            tmpRes = []
            for idx in range(qLen):
                curr = queue.popleft()
                if curr:
                   tmpRes.append(curr.val)
                   queue.append(curr.left) 
                   queue.append(curr.right) 
                
            if tmpRes:
                res.append(tmpRes)

        return res
        
