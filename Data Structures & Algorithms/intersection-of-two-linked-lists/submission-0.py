# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
      
        # 1. 特判：只要有一个链表为空，一定不相交
        if not headA or not headB:
            return None
        
        # 2. 初始化两个指针，分别指向两个链表的头
        pA = headA
        pB = headB
        
        # 3. 关键循环：当两个指针不相等时，继续移动
        while pA != pB:
            # 如果 pA 走到头了，就切换到 headB（消除长度差）
            # 否则正常走下一步
            pA = pA.next if pA else headB
            # 如果 pB 走到头了，就切换到 headA
            pB = pB.next if pB else headA
        
        # 4. 循环结束时，pA 和 pB 要么同时为 None（不相交），要么指向相交节点
        return pA