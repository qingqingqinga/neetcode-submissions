class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            distance = r - l
            if l < r and heights[l] < heights[r]:
                area = heights[l] * distance
                max_area = max(area, max_area)
                l += 1

            
            else:
                area = heights[r] * distance
                max_area = max(max_area, area)
                r -= 1
            
        return max_area





        

        
