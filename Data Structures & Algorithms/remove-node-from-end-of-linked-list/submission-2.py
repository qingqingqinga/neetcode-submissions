# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#很容易想 但可以优化的解法
#优化解法在leetcode上
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """




        dummy = ListNode(next = head)
        length = 0 
        cur  = head
        while cur:
            length += 1
            cur = cur.next
        
        node = dummy
        #head
        #倒数1        length - 1
        #倒数2        length - 2
        #倒数n + 1        length - (n + 1) 

        #必须用dummy保证头节点也能正确删除



        for _ in range(length - n):
            node = node.next
        
        node.next = node.next.next

        return dummy.next
        


        