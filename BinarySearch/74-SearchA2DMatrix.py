from typing import List

# Time : O( n* m)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #number of row
        m = len(matrix)
        # number of column
        n = len(matrix[0])
        t = m * n
        l = 0
        r = t - 1

        while l <= r:
            m = (l+r)//2
            i = m // n
            j = m % n

            mid_num = matrix[i][j]

            if mid_num == target:
                return True
            elif target < mid_num:
                r = m - 1
            else:
                l = m + 1
        return False

# Time : O(log(m*n))
# Space : O(1)