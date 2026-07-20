from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        result = []
        while left <= right:
            #we use abs to compare, this is easier than Square
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left]**2)
                left += 1
            else:
                result.append(nums[right]**2)
                right -= 1

        result.reverse()
        return result

    #Time : O(n)
    #Space : O(n) (result is the only storage, so we can say it's O(1)
