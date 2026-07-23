from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_counts = [0] * (n + 1)
        for c in citations:
            # min(n,c) is for edge case where citations > n
            # The last index represents the number of papers with n or more citations
            paper_counts[min(n,c)] += 1
        h = n
        papers = paper_counts[n]

        while papers < h:
            h -= 1
            papers += paper_counts[h]

        return h

# Time : O(n)
# Space : O(n)
