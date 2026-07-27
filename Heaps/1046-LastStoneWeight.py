from typing import List
#heapq = min heap
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            #To use a max heap, we invert the List
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)

            if largest != next_largest:
                heapq.heappush(stones, largest - next_largest)

        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0
# Time : O(n log n)
# Space : O(1)
