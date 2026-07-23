
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bubble sort : O(n²)
        # Quick sort or merged sort : O(n log n) on average
        # Counting sort : O( n +k) where k is the numbers of differents numbers (here k =3)
        #                 Space : O(k)

        #Another solution : DNF : Deutsch National Flag : Time : O(n) and space : O(1)

        counts = [0, 0, 0]

        for color in nums:
            counts[color] += 1

        R, W, B = counts
        nums[:R] = [0]* R
        nums[R:R+W] = [1]* W
        nums[R+W:] = [2]* B

        # Time : O(n + k)
        # Space : O(k) = O(3) = O(1)



