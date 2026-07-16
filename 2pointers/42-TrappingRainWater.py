"""
trick :
prendre la hauteur max et hauteur min à chaque trou (par rapport à toutes les hauteurs)
min(hmin, hmax) = case d'eau retenue
si pas un trou à 0 mais plus haut, même tecnique mais en soustrayant la hauteur du fossé
on fait donc ça pour chaque colonne(chaque position), si le résultat de min - height est négatif, on ne peut pas avoir d'eau
les deux extrémités ne stockent pas d'eau
pour chaque position, on doit donc connaitre hauteur max à gauche et à droite => stocké dans un array
on remplit le tableau avant de vérifier si on peut remplir d'eau
"""
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] *n
        max_right = [0] *n

        for i in range(n):
            j = -i -1 #-1 = last index
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        summ = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            #si différence négative, on ne stocke pas d'eau => +0
            summ += max(0, pot-height[i])
        return summ

#Time : O(n)
#Space : O(n) 2 pointer
