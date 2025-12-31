# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Construct the stack and iterate the sum from the back
        s1, s2 = [], []
        cur = l1
        while cur:
            s1.append(cur)
            cur = cur.next
        cur = l2
        while cur:
            s2.append(cur)
            cur = cur.next
        r, head = 0, None
        while s1 or s2:
            val = r
            if s1: val += s1.pop().val
            if s2: val += s2.pop().val
            r = val // 10
            val = val % 10
            head = ListNode(val=val, next=head)
        if r:
           head = ListNode(val=r, next=head)
        return head