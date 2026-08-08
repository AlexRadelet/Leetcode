from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Bottom up DP (Tabulation)
        # Time : O(n²) => Using binary search, O(n log n )
        # Space : O(n)
        n = len(nums)
        dp = [1] *n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)