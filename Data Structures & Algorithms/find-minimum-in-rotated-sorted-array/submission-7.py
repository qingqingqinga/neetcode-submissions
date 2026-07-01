class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r + l) // 2
            if nums[l] < nums[r]:
                return nums[l]
            
            elif nums[mid] < nums[l]:
                r = mid
            
            elif nums[mid] > nums[r]:
                l = mid + 1
        return nums[l]

        l, r = 0, len(nums)
        while l < r:
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


