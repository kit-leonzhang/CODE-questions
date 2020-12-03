import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        i = 0
        while queue:
            n = len(queue)
            for k in range(n):
                node = queue.popleft()
                if node:
                    queue.extend([node.left, node.right])
            i += 1
        return i - 1


    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth2(root.left), self.maxDepth2(root.right)) + 1


if __name__ == "__main__":
    r = TreeNode(1)
    #r.left = TreeNode(2)
    r.right = TreeNode(2)
    #r.right.right = TreeNode(3)
    S = Solution()
    print(S.maxDepth2(r))