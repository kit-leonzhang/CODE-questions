class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.maxDepth2(root.left) - self.maxDepth2(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth2(root.left), self.maxDepth2(root.right)) + 1


if __name__ == "__main__":
    d = TreeNode(1)
    d.right = TreeNode(2)
    d.right.left = TreeNode(2)
    d.right.left.left = TreeNode(2)
    S = Solution()
    print(S.isBalanced(d))