from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        #at least one value in the array
        closest = nums[0]
        for x in nums:
            if abs(x)<abs(closest):
                closest = x
        if closest <0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
#Time : O(2n)
#Space : O(1)