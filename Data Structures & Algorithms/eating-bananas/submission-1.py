class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # expected approach: binary search 
        lower = 1 
        upper = max(piles)
        speed = max(piles)
        while lower <= upper:
            mid = (lower + upper) // 2
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / mid)
            if totalHours > h:
                lower = mid + 1
            else:
                speed = mid
                upper = mid - 1
        return speed




        