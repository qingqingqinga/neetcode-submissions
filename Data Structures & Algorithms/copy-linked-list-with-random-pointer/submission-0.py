"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        复制一个带随机指针（random）的链表。
        
        核心思路（分两步走）：
        1. 第一遍遍历：只克隆节点（复制值），暂不处理指针。把所有 <原节点, 新节点> 的映射存进哈希表。
        2. 第二遍遍历：利用哈希表，把克隆节点的 next 和 random 指向对应的克隆节点。
        
        为什么不能一次遍历完成？
        因为 random 指针可能指向后面还没创建的节点。如果遇到一个 random 指向未来的节点，此时该节点还没被克隆，就无法正确赋值。
        所以必须先把所有节点都造出来，再统一连线。
        """

        if not head:
            return None
        # 
        oldToCopy = {}

        cur = head
        # 第一次循环：遍历原链表，只复制节点的值，生成新节点
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        # --- 第二步：再次遍历原链表，用哈希表搭建新链表的指针关系 ---
        cur = head
        while cur:
            copy = oldToCopy[cur]

            # 【处理 next 指针】
            # cur.next 是原节点的下一个节点
            # oldToCopy.get(cur.next) 的作用：
            #   - 如果 cur.next 不是 None，就去哈希表里找它对应的新节点
            #   - 如果 cur.next 是 None，.get(None) 会返回 None（不会报错）
            # 然后把找到的新节点（或 None）赋值给 copy 的 next
            copy.next = oldToCopy.get(cur.next)

            # 【处理 random 指针】
            # 逻辑完全同上：根据原节点的 random 指向的原节点，去哈希表里找到对应的新节点
            copy.random = oldToCopy.get(cur.random)

            # 继续处理下一个原节点
            cur = cur.next

        # --- 返回新链表的头节点 ---
        # oldToCopy[head] 就是原头节点对应的新建头节点，整个新链表从这里开始
        return oldToCopy[head]

        
        