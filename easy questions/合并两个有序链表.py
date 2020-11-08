class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2  # 终止条件，直到两个链表都空
        if not l2:
            return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    L1 = ListNode(1)
    L1.next = ListNode(2)
    L1.next.next = ListNode(4)
    L2 = ListNode(1)
    L2.next = ListNode(3)
    L2.next.next = ListNode(4)
    S = Solution()
    print(S.mergeTwoLists(L1, L2).next.next.val)


