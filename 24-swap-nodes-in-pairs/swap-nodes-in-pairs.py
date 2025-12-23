# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        returnHead = head
        while cur and cur.next:
            # Need to swap the head
            if cur == returnHead:
                returnHead = cur.next
            # Get the target swap and next cursor location
            targetSwap, nextCur = cur.next, cur.next.next
            # Swap the node
            targetSwap.next = cur
            cur.next = nextCur
            # Update the previous node to point to the new node
            if prev:
                prev.next = targetSwap
            # Prepare for next iteration
            prev = cur
            cur = nextCur
        return returnHead