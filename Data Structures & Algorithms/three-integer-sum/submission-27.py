class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#只在 找到一组解并移动指针之后 才跳过重复的 l 和 r。
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i > 0  and nums[i] == nums[i - 1]:
                continue
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] <= 0:
                    l += 1
                else:
                    r -= 1
        return res
        