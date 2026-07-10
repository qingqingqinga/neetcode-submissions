class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #在插入 nums[0] 时，如果子排列 p 中已经有与 nums[0] 相同的元素，
        #那么只允许插入到第一个相同元素的后面，避免生成重复排列。
        # 递归基：空数组只有一种排列
        if len(nums) == 0:
            return [[]]
        
        # 取出第一个元素（不需要先排序）
        first = nums[0]
        
        # 子问题：剩余元素的所有排列（假设已经完美算好）
        perms = self.permuteUnique(nums[1:])
        
        res = []
        for p in perms:
            # ---------- 核心去重逻辑 ----------
            # 找到 p 中 最后一个 等于 first 的元素的索引
            last_idx = -1
            for idx, val in enumerate(p):
                if val == first:
                    last_idx = idx
            
            # 只有从这个位置之后（严格大于 last_idx）才能插入
            # 如果 p 中没有 first，last_idx 为 -1，则从 0 开始插入所有位置
            start_i = last_idx + 1
            
            for i in range(start_i, len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, first)
                res.append(p_copy)
        
        return res
       