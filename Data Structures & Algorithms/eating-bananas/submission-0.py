class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        for k in range(1,max_k + 1):
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
            if hours <= h:
                return k
            
       
        