import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        a = []
        if not root:
            return a
        else:
            queue = collections.deque()
            queue.append((root.left, root.right))
            a = [[root.val]]
            while queue:
                b = []
                for i in range(len(queue)):
                    left, right = queue.popleft()
                    if not left and not right:
                        continue
                    if left and not right:
                        b.append(left.val)
                        queue.append((left.left, left.right))
                    if not left and right:
                        b.append(right.val)
                        queue.append((right.left, right.right))
                    if left and right:
                        b.extend([left.val, right.val])
                        queue.extend([(left.left, left.right), (right.left, right.right)])
                if b:
                    a.append(b)
            return a[::-1]


if __name__ == "__main__":
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(2)
    r.right.right = TreeNode(3)
    r.left.right = TreeNode(4)
    r.left.left = TreeNode(5)
    S = Solution()
    print(S.levelOrderBottom(r))