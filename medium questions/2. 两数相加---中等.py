# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        S1 = 0
        S2 = 0
        i = 0
        j = 0
        while l1:
            S1 += l1.val * (10 ** i)
            l1 = l1.next
            i += 1
        while l2:
            S2 += l2.val * (10 ** j)
            l2 = l2.next
            j += 1
        S = S1 + S2
        if S == 0:
            LL = ListNode(0)
            return LL
        LL = ListNode(S % 10)
        a = LL
        S = S // 10
        while S > 0:
            a.next = ListNode(S % 10)
            a = a.next
            S = S // 10
        return LL


if __name__ == "__main__":
    r = ListNode(2)
    r.next = ListNode(4)
    r.next.next = ListNode(3)
    o = ListNode(5)
    o.next = ListNode(6)
    o.next.next = ListNode(4)
    #o.next.next.next = ListNode(9)
    S = Solution()
    print(S.addTwoNumbers(r, o).next.val)