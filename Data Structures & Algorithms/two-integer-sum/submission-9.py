class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap={} # num:index

        for i in range(len(nums)):
            num=nums[i]
            diff=target-num

            if diff in preMap:
                return [preMap[diff],i]
            preMap[num]=i
        return []
        