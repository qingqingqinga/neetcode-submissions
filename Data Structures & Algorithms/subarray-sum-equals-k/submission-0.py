class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 哈希表：key 是前缀和，value 是该前缀和出现的次数
        # 初始化：前缀和为 0 出现过 1 次（代表空前缀）
       

        prefix_sum_count = {0: 1}
        
        cur_sum = 0  # 记录当前累加的前缀和
        res = 0      # 记录满足条件的子数组个数
        
        for num in nums:
            # 1. 更新当前前缀和
            cur_sum += num
            
            # 2. 核心逻辑：查找 cur_sum - k 在之前出现过几次
            # 如果有，说明从那个位置+1 到当前位置的子数组和为 k
            if (cur_sum - k) in prefix_sum_count:
                res += prefix_sum_count[cur_sum - k]
            
            # 3. 将当前前缀和存入哈希表，供后续使用
            prefix_sum_count[cur_sum] = prefix_sum_count.get(cur_sum, 0) + 1
            
        return res
