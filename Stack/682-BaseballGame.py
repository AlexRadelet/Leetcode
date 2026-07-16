from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for op in operations:
            if op == '+':
                stk.append(stk[-1] + stk[-2])
            elif op == 'D':
                stk.append(stk[-1] * 2)
            elif op == 'C':
                stk.pop()
            #Si ce n'est pas un des 3 premiers cas, c'est un nombre (pas besoin de try catch)
            else:
                stk.append(int(op))
        #sum of empty list is 0
        return sum(stk)
