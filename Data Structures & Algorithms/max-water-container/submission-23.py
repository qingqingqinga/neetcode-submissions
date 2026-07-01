class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            distance = r -l
            if heights[l] >= heights[r]:
                cur_area = distance * heights[r]
                max_area = max(cur_area, max_area)
                r -= 1
            else:
                cur_area = distance * heights[l]
                max_area = max(cur_area, max_area)
        
                l += 1
        return max_area

      







