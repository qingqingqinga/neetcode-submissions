class Solution:
    def jump(self, nums: List[int]) -> int:
        
       

        res = 0
        l = 0
        r = 0
        n = len(nums)
        
        while r < n - 1: #重点
            farthest = 0
            # 遍历当前这一跳所能覆盖的所有位置
            for i in range(l, r + 1): #重点
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
