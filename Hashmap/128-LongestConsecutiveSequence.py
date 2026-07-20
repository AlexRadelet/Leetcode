from typing import List
#With sorting, Time : O(n*log(n))
        # Better with a set, at each number check if there is num-1 or num+1
        # Idea : check only num-1 to find th start of a sequence => Time : O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)

        return longest
    #Time : O(n)
    #Space : O(n)