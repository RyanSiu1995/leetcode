# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Simple solution: sort linked list out of the box
        if not head or not head.next: return head
        nodes, cur = [], head
        while cur:
            nodes.append(cur)
            cur = cur.next
        nodes.sort(key=lambda x: x.val)
        for i in range(len(nodes)):
            if i + 1 > len(nodes) - 1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i+1]
        return nodes[0]
