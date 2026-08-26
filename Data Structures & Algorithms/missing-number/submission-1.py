class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)
        for i in range(len(nums) + 1):
            if i not in hashset:
                return i
        n = len(nums)
        total = (n + 1) * (n + 0) //2
        missing_number = total - sum(nums)
        return missing_number
        #高斯公式 i = 1 到 i= n 为 （n个数）*（ n最后一个数 + 1第一个数） // 2
        #这一题里面 i = 0 到 i = n （有n+1 的总数）（n最后一个数 + 0第一个数）//2 