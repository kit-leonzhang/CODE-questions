class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if nums:
            m = len(nums)//2
            r = TreeNode(nums[m])
            r.left = self.sortedArrayToBST(nums[:m])
            r.right = self.sortedArrayToBST(nums[m+1:])
            return r


if __name__ == "__main__":
    a = [1]
    S = Solution()
    rr = S.sortedArrayToBST(a)
    print(rr.val)