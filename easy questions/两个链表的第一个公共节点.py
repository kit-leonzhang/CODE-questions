class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha


if __name__ == "__main__":
    L3 = ListNode(8)
    L3.next = ListNode(4)
    L3.next.next = ListNode(5)
    L1 = ListNode(4)
    L1.next = ListNode(1)
    L1.next.next = L3
    L2 = ListNode(5)
    L2.next = ListNode(0)
    L2.next.next = ListNode(1)
    L2.next.next.next = L3
    S = Solution()
    print(S.getIntersectionNode(L1, L2).val)