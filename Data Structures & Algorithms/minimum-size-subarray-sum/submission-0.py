class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0               # 左指针，窗口左边界
        total = 0         # 当前窗口内元素的和
        min_len = float('inf')   # 最短长度初始化为无穷大


        for r in range(len(nums)):
            total = total + nums[r]
            while total >= target:
                min_len = min(min_len, r - l + 1)
                total = total - nums[l]
                l += 1
        
        return min_len if min_len != float('inf') else 0



        