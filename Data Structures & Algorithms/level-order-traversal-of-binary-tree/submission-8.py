class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
       

        ans = []
        q = deque([root]) #参数 iterable 是一个可迭代对象（如列表、元组、字符串等），其元素会被逐个添加到 deque 中。

#如果您传入一个非可迭代对象（例如一个 TreeNode 实例），Python 会尝试对其进行迭代（调用 __iter__），但 TreeNode 类并未实现迭代协议，因此会抛出 TypeError: 'TreeNode' object is not iterable。
       
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft() #先要popleft出来
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals)
        return ans
    