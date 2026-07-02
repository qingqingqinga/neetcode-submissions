# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        if not list:
            return []
        for l in lists:
            i = l
            while i:
                nums.append(i.val)
                i = i + 1
        
        nums.sort()
        dummy = ListNode(next = cur)
        for i in range(len(nums)):
            cur = ListNode(nums[i])
            cur = cur.next
        return dummy.next
        