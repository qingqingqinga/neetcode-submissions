class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #56leetcode 合并区间
        # hashmap key: value [26] : [start,end]
        # ---------- 第一步：求出每个字母的 [首次出现, 最后出现] 区间 ----------
        # 使用 defaultdict 简化写法，存储 [start, end]
        intervals = defaultdict(lambda: [float('inf'), float('-inf')])

        for i, ch in enumerate(s):
            # 如果是第一次遇到，更新 start
            if intervals[ch][0] == float('inf'):
                intervals[ch][0] = i
            # 每次都更新 end（因为遍历是递增的，实际上可以直接赋值 i）
            intervals[ch][1] = i

        # 提取所有区间，并按 start 排序（LeetCode 56 的前置要求）
        # 注意：这里用 ch 作为 key 排序其实没必要，直接取 values 排序即可
        interval_list = sorted(intervals.values(), key=lambda x: x[0])

        # ---------- 第二步：完全套用 LeetCode 56 的合并区间模板 ----------
        merged = []
        for start, end in interval_list:
            # 如果 merged 为空，或者当前区间与上一个不重叠
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                # 重叠则合并，更新最大右边界
                merged[-1][1] = max(merged[-1][1], end)

        # ---------- 第三步：将合并后的区间长度转化为答案 ----------
        res = []
        for start, end in merged:
            res.append(end - start + 1)
        return res

            
