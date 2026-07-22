from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] < target:
                # We are looking on the right side
                l = mid + 1
            elif nums[mid] > target:
                # We are looking on the left side
                r = mid - 1
            else:
                return mid
        if nums[mid] < target:
            return mid +1
        else:
            return mid

# Time : O(log n)
#Space : O(1)


