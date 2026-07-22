# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

#Condition base binary search
class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n
        #We want to leave when L == R
        while L < R:
            M = (L + R) // 2
            if isBadVersion(M):
                R = M
            else:
                L = M + 1
        return L

# Time : O(log n)
# Space : O(1)