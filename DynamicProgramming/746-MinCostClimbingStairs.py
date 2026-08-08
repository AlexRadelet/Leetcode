from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top Down DP Memoization
        # n = len(cost)
        # memo={0:0,1:0}
        # def min_cost(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] =  min(cost[i-2] + min_cost(i-2), cost[i-1] + min_cost(i-1))
        #         return memo[i]
        # return min_cost(n)

        # Bottom Up Tabulations
        # n = len(cost)
        # dp = [0]*(n+1)
        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        # return dp[n]
        # Bottom Up Constant space
        n = len(cost)
        prev, cur = 0,0
        for i in range(2, n + 1):
            prev, cur = cur, min(cost[i - 2] + prev, cost[i - 1] + cur)
        return cur

