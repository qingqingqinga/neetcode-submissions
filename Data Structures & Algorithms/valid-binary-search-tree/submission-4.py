# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node,left,right):
            if node is None:
                return True
            x = node.val

            return left < x < right and dfs(node.left,left,x) and dfs(node.right,x,right)
        return dfs(root,float('-inf'),float('inf'))

