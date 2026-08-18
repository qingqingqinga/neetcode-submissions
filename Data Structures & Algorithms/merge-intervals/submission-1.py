class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 1. 边界情况：空数组
        if not intervals:
            return []
        

        intervals.sort(key = lambda x: x[0])

        
        # 3. 初始化结果集，先把第一个区间放进去
        merged = [intervals[0]]
        
        # 4. 线性扫描合并
        for i in range(1, len(intervals)):

            # 当前结果集中最后一个区间
            start, end = intervals[i]
            prev_start, prev_end = merged[-1]

            
            # 如果当前区间的左端点 <= 上一个区间的右端点，说明重叠
            if start <= prev_end:
                # 合并：更新上一个区间的右端点（取两者最大值，防止完全包含）
                merged[-1][1] = max(prev_end, end)
            else:
                # 不重叠，直接追加
                merged.append([start, end])
                
        return merged
        

        