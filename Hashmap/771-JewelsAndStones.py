class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #Brut force : Time : O(n *m)
        # With set, Time : O(n+m)
        #Space : O(n)
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count