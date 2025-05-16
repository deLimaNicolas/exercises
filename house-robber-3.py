#337. House Robber III
#The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
#
#Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
#Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

#Input: root = [3,2,3,null,3,null,1]
#Output: 7
#Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7
#                   3 
#            2            3 (3 + max(notRobLeft) + maxNotRob(right), max(notRoball))
#         _     3      _ (0, 0)    1 (1, 0)
#
# in the example above the correct way would be 3 + 3 + 1 and in order to get this
# I'm basically comparing what would happen if I sum or dont sum (rob) each house 

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

e    = TreeNode(3, None, None)
b    = TreeNode(2, None, e)
g    = TreeNode(1, None, None)
c    = TreeNode(3, None, g)
root = TreeNode(3, b, c)

# Time complexity O(n) space complexity is pretty much the tree height

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def rob(self, root: Optional[TreeNode]) -> int:
        def check_higher_path(node: Optional[TreeNode]):
            if not node:
                return [0, 0]  # [rob, not_rob]
            
            left = check_higher_path(node.left)
            right = check_higher_path(node.right)
            
            # If we rob this node, we can't rob its children
            rob_current_node = node.val + left[1] + right[1]
            
            # If we don't rob this node, we can choose the max from each child
            not_rob_current_node = max(left[0], left[1]) + max(right[0], right[1])
            
            return [rob_current_node, not_rob_current_node]
        
        result = check_higher_path(root)
        return max(result)
def main():
    solution = Solution()
    result = solution.rob(root)
    print(result)

if __name__=="__main__":
    main()


