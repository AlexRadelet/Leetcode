from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, value in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                heapq.heappushpop(heap, (value, key))
        #h[1] = key, the number we want
        return [h[1] for h in heap]

# Time : O(n * log k)
# Space : O(n)

