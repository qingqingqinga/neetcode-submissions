class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 区间为 [left, right]，左右都闭合
        
        while left <= right:     
            mid = left + (right - left) // 2 
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1          # target 在右半边，排除 mid
            else:
                right = mid - 1         # target 在左半边，排除 mid.    
        return left
        
                              # 没找到

        