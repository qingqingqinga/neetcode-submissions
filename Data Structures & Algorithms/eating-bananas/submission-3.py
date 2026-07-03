class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        left = 1
        right = max_pile

        while left <= right:
            mid = left + (right - left) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left

