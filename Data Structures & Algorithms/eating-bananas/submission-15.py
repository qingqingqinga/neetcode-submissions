class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        left = 1
        right = max_pile
        res = right

        while left <= right:
            mid = (left + right ) //2
            hour = 0
            for i in range(len(piles)):
                hour += math.ceil(piles[i] / mid)
            if hour <= h:
                res = min(res,mid)
                right = mid - 1
            else:
                left = mid + 1
            
            #非常重点 这样是错误的 反着的  
            #if hour >= h:
            #    res = min(res,mid)
            #    left = mid + 1
            #else:
             #   right = mid - 1
        return res

 