from typing import List
from math import ceil, floor

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t in "+-*/":
                #Order is important, b is the first things we pop ( a * b for example)
                b, a = stk.pop(), stk.pop()

                if t == '+':
                    stk.append(a + b)
                elif t == '-':
                    stk.append(a - b)
                elif t == '*':
                    stk.append(a * b)
                else:
                    # division could be a float, no integer division ( a //b)
                    division = a / b
                    if division < 0:
                        stk.append(ceil(division))
                    else:
                        stk.append(floor(division))
            else:
                stk.append(int(t))
        # There is only one number in the stack at the end
        return stk[0]

# Time : O(n)
# Space : O(n)
