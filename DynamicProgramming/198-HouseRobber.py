from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top Down DP memoization
        # n = len(nums)
        # if n ==1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0],nums[1])
        #
        # memo = {0:nums[0], 1:max(nums[0],nums[1])}
        # def helper(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = max(nums[i] + helper(i-2), helper(i-1))
        #         return memo[i]
        #
        # return helper(n-1)
        # Bottom Up DP Tabulation
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])
        #
        # dp = [0]*n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        # return dp[n-1]
        # Bottom Up DP Constant Space
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])


        prev = nums[0]
        curr = max(nums[0], nums[1])
        for i in range(2, n):
            prev, curr = curr, max(prev + nums[i], curr)
        return curr


