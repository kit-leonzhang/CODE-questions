class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if self.isleaf(root):
            return root.val == sum
        if root.left and not root.right:
            if self.isleaf(root.left):
                return root.left.val + root.val == sum
            else:
                return self.hasPathSum(root.left, sum - root.val)
        if root.right and not root.left:
            if self.isleaf(root.right):
                return root.right.val + root.val == sum
            else:
                return self.hasPathSum(root.right, sum - root.val)
        if root.right and root.left:
            if self.isleaf(root.right) and self.isleaf(root.left):
                return root.right.val + root.val == sum or root.left.val + root.val == sum
            if self.isleaf(root.left) and not self.isleaf(root.right):
                return root.left.val + root.val == sum or self.hasPathSum(root.right, sum - root.val)
            if self.isleaf(root.right) and not self.isleaf(root.left):
                return root.right.val + root.val == sum or self.hasPathSum(root.left, sum - root.val)
            return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def isleaf(self, leaf: TreeNode):
        if not leaf.left and not leaf.right and leaf:
            return True
        else:
            return False


if __name__ == "__main__":
    r = TreeNode(1)
    r.left = TreeNode(4)
    r.left.left = TreeNode(-2)
    #r.left.left.left = TreeNode(4)
    #r.left.left.left.left = TreeNode(5)
    S = Solution()
    print(S.hasPathSum(r, 3))