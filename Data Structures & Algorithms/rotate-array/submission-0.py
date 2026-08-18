class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 关键步骤：取模，防止 k 大于 n
        k = k % n
        
        # 辅助函数：反转 nums[l..r] 区间（闭区间）
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]  # 交换左右两端
                l += 1
                r -= 1
        
        # 三次反转
        reverse(0, n - 1)    # 反转整个数组
        reverse(0, k - 1)    # 反转前 k 个
        reverse(k, n - 1)    # 反转后 n-k 个