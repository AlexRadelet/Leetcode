from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stk and height < stk[-1][0]:
                h, j = stk.pop()
                w = i - j
                a = h*w
                max_area = max(a, max_area)
                start = j
            # We need to go backward if th height is ok
            stk.append((height, start))

        while stk:
            h, j = stk.pop()
            w = n - j
            max_area = max(h*w, max_area)

        return max_area

    # Time : O(n)
    # Space : O(n)