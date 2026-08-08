class Solution:
    def climbStairs(self, n: int) -> int:
        # Top Down Memoization
        # memo = {1:1,2:2}
        # def f(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = f(n-2) + f(n-1)
        #         return memo[n]
        # return f(n)

        # Bottom Up Tabulation
        # if n == 1: return 1
        # if n == 2: return 2
        # # n, not n+1, because base case starts at 1, not at 0
        # dp = [0]*(n)
        # dp[0] = 1
        # dp[1] = 2
        # for i in range(2, n):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n-1]
    # Bottom Up Tabulation with 2 variables
        if n == 1: return 1
        if n == 2: return 2
        # n, not n+1, because base case starts at 1, not at 0
        prev = 1
        cur = 2
        for i in range(2, n):
            prev, cur = cur, prev + cur
        return cur



