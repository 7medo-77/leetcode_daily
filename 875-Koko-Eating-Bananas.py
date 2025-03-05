from functools import reduce
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        resultArray = []
        if (h == len(piles)):
            return max(piles)
        else:
            # bananaRateArray = [rate for rate in range(1, max(piles) + 1)]
            left = 1
            # right = len(bananaRateArray) - 1
            right = max(piles)

            while left <= right:
                mid = (left + right) // 2
                allHoursToEat = 0

                for number in piles:
                    hourToEat = math.ceil(number / mid)
                    allHoursToEat += hourToEat

                if allHoursToEat <= h:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
