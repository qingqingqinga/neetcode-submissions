# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        if not lists:
            return []
        for l in lists:
            i = l
            while i:
                nums.append(i.val)
                i = i.next
        
        nums.sort()
        dummy = ListNode()
        cur = dummy.next

        for i in range(len(nums)):
            cur = ListNode(nums[i])
            cur = cur.next
        return dummy.next
        