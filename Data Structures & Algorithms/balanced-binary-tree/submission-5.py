# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       #重要 用maxdepth的思想 
       # 易错点 ： 1.需要根节点的左右子树平衡 2.根节点的左右子树的内部也必须平衡



        def get_height(node):
            if node is None:
                return 0
            l_height = get_height(node.left)
            if l_height == -1:
                return -1
            r_height = get_height(node.right)
            if r_height == -1 or abs(r_height - l_height) > 1:
                return -1
            
            return max(l_height,r_height) + 1
        return get_height(root)!= -1

        