from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = 'balloon'
        for c in text:
            #if not in c, it will be fixed to 0 => 0+1=1
            if c in balloon:
                counter[c] += 1
        #If there is c in balloon that doesn't appear in balloon
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])

# Time : O(n)
#Space : O(1) #We store b, a, l, o and n
