import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2
            # try if this rate works
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            if time > h:
                left = k + 1
            else:
                res = min(res, k)
                right = k - 1
        return res