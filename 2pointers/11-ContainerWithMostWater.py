"""
for i ...
    for j ...
Time : O(n²)

2 pointers : un pointeurà gauche et un à droite
A = W * H
Lorsqu'on déplace les pointeurs, on se rapproche du centre => on réduit W
On va donc de la plus grande à la plus petite W
On peut par contre choisir quel pointeur maintenir => On garde celui avec le plus grand H (toujours pour maximiser le volume
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        max_area = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = h * w
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l +=1
            else:
                r -=1
        return max_area

#Time : O(n)
#Space : O(1)