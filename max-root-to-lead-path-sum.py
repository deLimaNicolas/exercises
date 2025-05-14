# Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. 
# The function should return the maximum sum of any root to leaf path within the tree.
# You may assume that the input tree is non-empty.
#
#   a = Node(3)
#   b = Node(11)
#   c = Node(4)
#   d = Node(4)
#   e = Node(-2)
#   f = Node(1)
#   
#   a.left = b
#   a.right = c
#   b.left = d
#   b.right = e
#   c.right = f
#   
#          3
#       /    \
#      11     4
#     / \      \
#    4   -2     1
#   
#   max_path_sum(a) # -> 18

class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.left = None
        self.right = None

a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(0)
f = Node(-13)
g = Node(-1)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h


class Solution:
    def max_path_sum(self, root_node: Node) -> int:
        if not root_node:
            return float('-inf')

        if not root_node.left and not root_node.right:
            return root_node.val

        left_val = self.max_path_sum(root_node.left)
        right_val = self.max_path_sum(root_node.right)

        higher_val = left_val if left_val > right_val else right_val

        return root_node.val + higher_val

def main():
    solution = Solution()
    result = solution.max_path_sum(a)
    print(result)


if __name__=="__main__":
    main()

# Space complexity O(h)
# Time complexity O(n)
