class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not ( head.next ):
            return head
        elif head.val == head.next.val:
            head = head.next
            return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head


if __name__ == "__main__":
    S = Solution()
    A = ListNode(1)
    A.next = ListNode(1)
    A.next.next = ListNode(2)
    A.next.next.next = ListNode(3)
    A.next.next.next.next = ListNode(3)
    B = []
    print(S.deleteDuplicates(B))