class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
       

        ans = []
        q = deque([root])
       
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft() #先要popleft出来
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals)
        return ans
    