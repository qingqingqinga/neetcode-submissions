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

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            shorter_area = min(heights[l], heights[r])
            max_area = max(max_area,shorter_area * (r - l))

            if heights[l] >= heights[r]:
                max_area = max(max_area, heights[r] * (r - l))
                r -= 1
            else:
                max_area = max(max-area,heights[l] * (r - l))
                l += 1
        return max_area

            








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





        

        
