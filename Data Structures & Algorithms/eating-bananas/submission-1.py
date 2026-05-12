from math import *

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        search = range(1, max(piles) + 1)
        min_k = 1000000000

        low, high = 0, len(search) - 1
        while low <= high:
            mid = (low + high) // 2

            k = search[mid]
            min_hours = 0

            # Calculate if k worked
            for pile in piles:
                min_hours += ceil(pile / k)
            print(min_hours, k)
            if (min_hours <= h):
                min_k = min(min_k, k)
                high = mid - 1
            else:
                low = mid + 1
        
        return min_k
                
            
