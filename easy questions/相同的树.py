class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        else:
            if not (p and q):
                return False
            else:
                if p.val != q.val:
                    return False
                else:
                    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    S = Solution()
    A = TreeNode(1)
    A.left = TreeNode(2)
    B = TreeNode(1)
    print(S.isSameTree(A, B))