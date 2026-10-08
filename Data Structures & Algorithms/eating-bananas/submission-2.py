class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <=right:
            mid = (left + right)//2
            total_hours = 0
            for i in range(0, len(piles)):
                this_pile_hours = piles[i] % mid
                if this_pile_hours == 0:
                    this_pile_hours = piles[i] //mid
                elif this_pile_hours == piles[i]:
                    this_pile_hours = 1
                else:
                    this_pile_hours = (piles[i] // mid) + 1
                total_hours +=this_pile_hours
            if total_hours<=h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res