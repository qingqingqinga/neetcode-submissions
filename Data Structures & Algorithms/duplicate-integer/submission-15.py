class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap.add(nums[i])
        return False
            






    

