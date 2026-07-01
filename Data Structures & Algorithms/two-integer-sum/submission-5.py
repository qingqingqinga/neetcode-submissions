class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {} # val: index
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in preMap:
                return [preMap[diff],i]
            preMap[nums[i]]=i
        return
        
        