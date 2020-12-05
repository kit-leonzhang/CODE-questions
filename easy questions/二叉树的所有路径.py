class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list:
        if not root:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        sub_paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        return [str(root.val) + "->" + s for s in sub_paths]


if __name__ == "__main__":
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(2)
    r.right.right = TreeNode(3)
    S = Solution()
    print(S.binaryTreePaths(r))