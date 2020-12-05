class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        if not root.left and root.right:
            root.left = self.invertTree(root.right)
            root.right = None
            return root
        if root.left and not root.right:
            root.right = self.invertTree(root.left)
            root.left = None
            return root
        if root.left and root.right:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

    def invertTree2(self, root):
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


