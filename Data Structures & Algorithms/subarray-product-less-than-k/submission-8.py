class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: #非常重要的边界条件
            return 0
        l = 0
        res = 0
        total = 1
        for r in range(len(nums)):
            total *= nums[r]

            while total >= k:
                total = total // nums[l] #一定要用整数除法
                l += 1
            
            res += (r - l + 1)
        return res
        