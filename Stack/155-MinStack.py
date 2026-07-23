# We will create 2 stacks, the second is to track the minimum
# Example : [5, 4, -1, 10]
#S = [5, 4, -1, 10]
#M = [5, 4, -1, -1] (minimum)
class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, value: int) -> None:
        self.stk.append(value)

        if not self.min_stk:
            self.min_stk.append(value)
        elif self.min_stk[-1] < value:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(value)

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]

    # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()