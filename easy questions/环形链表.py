class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        a = head
        b = []
        while a:
            if a in b:
                return True
            b.append(a)
            a = a.next
        return False


if __name__ == "__main__":
    h = ListNode(3)
    h.next = ListNode(2)
    h.next.next = ListNode(0)
    h.next.next.next = ListNode(-4)
    h.next.next.next.next = h.next
    s = Solution()
    print(s.hasCycle(h))
