# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        serialization = []

        def dfs(curr):
            if not curr:
                return
            serialization.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)

        return "-".join(serialization)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return []
        binary_elements = data.split("-")
        binary_integers = [int(elm) for elm in binary_elements]
        root = TreeNode(binary_integers[0])

        def add(curr, elm):
            if not curr:
                return TreeNode(elm)
            if curr.val > elm:
                curr.left = add(curr.left, elm)
            elif curr.val < elm:
                curr.right = add(curr.right, elm)
            return curr
        for elm in binary_integers[1:]:
            add(root, elm)
        
        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
