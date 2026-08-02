from typing import List

# Vu qu'on a besoin de 2 nombres, lorsqu'il ne reste que 2 nombres à choisir, on les prend obligatoirement
# Sur les 2 derniers étages de l'arbre, on ne prend pas les chemins de gauche ( voir exemple dans les notes)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, sol = [], []
        #x is a integer, not and index
        def backtrack(x):
            if len(sol) == k:
                ans.append(sol[:])
                return
            # Calculate if we go down or not
            left = x
            still_need = k - len(sol)
            if left > still_need:
                backtrack(x - 1)

            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)
        return ans

# Time : O(N choose k)
# Space : O(N)


