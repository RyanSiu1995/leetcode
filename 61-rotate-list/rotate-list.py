# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not k:
            return head
        # Find the node count and end
        nodeCount, cur = 1, head
        while cur.next:
            nodeCount += 1
            cur = cur.next
        # Find the target index node of new tail
        targetIdx = nodeCount - k % nodeCount - 1
        # If no move, return directly
        if not (targetIdx + 1):
            return head
        # Connect the tail to head
        cur.next = head
        # Find the new head and tail
        newCur = head
        for _ in range(targetIdx):
            newCur = newCur.next
        out = newCur.next
        newCur.next = None
        return out