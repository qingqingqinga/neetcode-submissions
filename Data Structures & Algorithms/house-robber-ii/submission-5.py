class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0],nums[1])
        
        def dfs(nums):
            m = len(nums)
            prev2 = nums[0]
            prev1 = max(nums[0],nums[1])

            for i in range(2,m):
                res = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = res
            return prev1
        return max(dfs(nums[1:n]),dfs(nums[0:n -1]))
        