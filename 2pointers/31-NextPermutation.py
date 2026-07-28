from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        # 1. Trouver le pivot :
        # premier indice i en partant de la droite tel que nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Si un pivot existe
        if i >= 0:

            # Chercher le plus petit élément > nums[i] en partant de la droite
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Échanger pivot et successeur
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Inverser la partie droite
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1