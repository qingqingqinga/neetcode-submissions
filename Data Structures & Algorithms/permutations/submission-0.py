class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #构造递归函数的三要素
        #1确定递归到最后的条件 
        #假设我们已经拿到我们需要的子问题的答案
        #2让这个递归问题变小到无
        #3算法的主要逻辑

        res = []
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        #假设【2，3】【3，2】
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res




        