"""
Tips :
Vu que la liste est triée, on sait quelle direction prendre pour augmenter/diminuer la somme
déplacer l pointer => augmenter la somme
déplacer r pointer => diminuer la somme
On fait cette technique car on demande un " constant extra space"
EN time, O(n), pas le plus opti => utiliser un hashmap sinon
"""

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1
        #on peut faire while car garantie d'avoir une solution unique
        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1,r+1]
            elif summ < target:
                l += 1
            else:
                r -= 1

