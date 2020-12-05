class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left and root.right:
            return self.minDepth(root.right) + 1
        if root.left and not root.right:
            return self.minDepth(root.left) + 1
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == "__main__":
    r = TreeNode(1)
    #r.left = TreeNode(2)
    r.right = TreeNode(2)
    r.right.right = TreeNode(2)
    S = Solution()
    print(S.minDepth(r))