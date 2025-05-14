#Write a function, tree_min_value, that takes in the root of a binary tree
#that contains number values.
#The function should return the minimum value within the tree.
#You may assume that the input tree is non-empty.

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
#tree_min_value(a) # -> -2

class Solution:
     # time complexity O(n) space complexity O(h)
    def tree_min_value(self, root_node):
        if root_node is None:
            return float("inf")

        left_min = self.tree_min_value(root_node.left)
        right_min = self.tree_min_value(root_node.right)

        return min(root_node.val, left_min, right_min)

class Solution2:
    def tree_min_value(self, root_node):
     # time complexity O(n) space complexity O(n)
        min_value = float("inf")
        stack = [root_node]

        while len(stack):
            current_node = stack.pop()

            min_value = min(
                current_node.val,
                min_value
            )

            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

        return min_value




def main():
    solution = Solution2()
    result = solution.tree_min_value(a)
    print(result)


if __name__=="__main__":
    main()


