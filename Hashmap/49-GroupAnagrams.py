from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs: #n
            count = [0] * 26
            for c in s:#m
                #ord("a") = 97, it's to attribuate the indexes of the letters
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())
    #Time : O(n*m)
    #Space : O(n*m)
