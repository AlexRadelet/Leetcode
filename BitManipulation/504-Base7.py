class Solution:
    def convertToBase7(self, num: int) -> str:
        if num ==0:
            return '0'

        original_number = num
        num = abs(num)
        remainders = []

        while num >0:
            remainder = num % 7
            remainders.append(str(remainder))
            num //= 7

        if original_number < 0:
            remainders.append('-')
        remainders.reverse()
        return ''.join(remainders)

# Time : O(log7 N)
# Space : O(log7 N)