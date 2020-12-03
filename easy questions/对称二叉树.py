import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append((root.left, root.right))
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True



if __name__ == "__main__":
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(2)
    S = Solution()
    print(S.isSymmetric(r))