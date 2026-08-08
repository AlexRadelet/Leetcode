class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Top Down DP Memoization
        # Time : O(m*n)
        # Space : O(m*n)
        # memo = {(0,0) : 1}
        # def paths(i,j):
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     elif i <0 or j <0 or i==m or j ==n:
        #         return 0
        #     else :
        #         val = paths(i-1,j) + paths(i,j-1)
        #         memo[(i,j)] = val
        #         return val
        #
        # return paths(m-1,n-1)

        # Down Up DP Tabulation
        dp = []
        for _ in range(m):
            dp.append([0] * n)

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                val = 0
                # Avoid first row
                if i > 0:
                    val += dp[i-1][j]
                # Avoid first column
                if j > 0:
                    val += dp[i][j-1]
                dp[i][j] = val
        return dp[m-1][n-1]



