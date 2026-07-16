from typing import List
#BruteForce => Time : O(n²)
#Pour une solution O(n), pour chaque index, on multiplie entre eux tout ce qu'il y a à gauche et tout ce qu'il y a droite
#Build 2 arrays, left and right arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #outside th array
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0]*n
        r_arr = [0]*n

        for i in range(n):
            #going forward and backwards in the same time
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        return [l*r for l, r in zip(l_arr, r_arr)]
#Time : O(n)
#Space : O(n) not optimal