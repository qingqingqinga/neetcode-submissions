# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        p0 = dummy
        pre = None
        cur = head
        while length >= k:
            length -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        
        return dummy.next
            

            
            
        
         




        