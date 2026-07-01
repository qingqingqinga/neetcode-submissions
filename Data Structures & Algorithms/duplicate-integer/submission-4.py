class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={} # key : val


        for num in nums:
            count[num]=1+count.get(num,0)
            if count[num]>1:
                return True
        return False
        


