from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        counter = {}
        for c in magazine:
            if c  in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        """
        #In a defaultdic, a value that doesn't exist will be set to 0
        counter = defaultdict(int)
        for c in magazine:
            counter[c] += 1

        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1
        return True
    #Time : O(m+m)
    #Space : O(m)

