from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours =0
            for p in piles:
                # hours taken per piles of bananas
                hours += ceil(p /k)
            # Return true if he cans eat the bananas in  h hours
            return hours <= h

        l = 1
        r = max(piles)

        # Binary search
        # If l <= r, it doesn't work, when l = r we found the answer
        while l < r:
            k = (l+r)//2
            if k_works(k):
                # We don't want to lose the value of k
                r = k
            else:
                # k doesn't work
                l = k + 1
        return r

# Time : O(n * log(max(piles))
# Space : O(1)