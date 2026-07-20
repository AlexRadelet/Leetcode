#One-Pass Hash Table
#O(n) : iterate once in the array, insertion and lookup time for a hash map is O(1)
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i
        return []