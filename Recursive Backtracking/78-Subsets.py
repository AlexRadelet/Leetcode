from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            # Don't pick nums[i]
            backtrack(i+1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            # Pop the same element that we append just before
            sol.pop()

        backtrack(0)
        return res

# Time : O(2^n)
# Space : O(n)
