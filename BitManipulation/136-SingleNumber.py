from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR is associative ( order doesn't matter)
        # a XOR a = 0
        # a XOR 0 = a
        # We will put the same numbers together
        a = 0
        for x in nums:
            a ^= x
        return a
    # Time = O(n)
    # Space : O(1)



