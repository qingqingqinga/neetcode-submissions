class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        prefix, postfix = 1, 1
        res = [1] * (len(nums))

        for i in range(len(nums)):

            res[i] = prefix #保存的是左侧的products 重要
            prefix = prefix * nums[i]

        
        for i in range(len(nums) - 1, -1, -1): #重要 倒序遍历是从n-1开始的
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

