# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0  # 空节点贡献为 0

            # 只取正贡献，负数直接舍弃
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # 经过当前节点的完整路径和（左+右+自己）
            current_path_sum = node.val + left_gain + right_gain
            self.maxSum = max(self.maxSum, current_path_sum)

            # 返回当前节点能贡献给父节点的最大单边值
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.maxSum
