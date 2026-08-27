class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 思路：
        # 1. 按区间起始时间升序排序，方便扫描。
        # 2. 用 end 记录当前保留的最后一个区间的结束时间。
        # 3. 遍历每个区间：
        # 若当前区间的 start >= end，说明不重叠，直接保留，更新 end = 当前区间的结束时间。
        # 若重叠，则必须删除一个区间。
        # 贪心原则：为了给后面的区间留更多空间，应该保留结束时间更小的那个区间。
        # 因此如果当前区间的结束时间 < end，就“替换”成当前区间（等价于删除了之前那个结束更晚的区间）。
        # 否则保留原区间（删除当前区间），end 不变。
        # 每次重叠计数 res++。
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])          # 按开始时间排序
        end = intervals[0][1]                       # 当前保留区间的结束时间
        res = 0

        for i in range(1, len(intervals)):
            start, cur_end = intervals[i]
            if start >= end:                        # 不重叠
                end = cur_end                       # 保留当前区间
            else:                                   # 重叠，必须删一个
                res += 1
                if cur_end < end:                   # 删掉原区间，保留当前区间（结束更早）
                    end = cur_end
                # 否则 end 不变，即删掉当前区间（结束更晚）
        return res
        