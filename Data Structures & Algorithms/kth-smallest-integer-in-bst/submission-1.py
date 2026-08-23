# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #和98题很像 inorder
        # 如果找到答案或者root is none就return
        # 第k小就是中序遍历的第几个 所以需要一个计数
        self.count = 0
        self.result = 0
        def dfs(root):
            if root is None or self.result:
                return 
            
            dfs(root.left)

            self.count += 1

            if self.count == k:
                self.result = root.val
                return
            
            dfs(root.right)
        dfs(root)
        return self.result
        