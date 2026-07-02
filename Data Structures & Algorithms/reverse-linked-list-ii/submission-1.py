# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        p0 = dummy
        
        for _ in range(left - 1):
            p0 = p0.next
        
        pre = None
        cur = p0.next

        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        
        p0.next.next = cur # 很容易错 p0.next 是2 现在2指向null 这里是把2这个节点指向cur
        p0.next = pre

        return dummy.next
        