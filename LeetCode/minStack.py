class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        
        # [-2, 0, 1, -3] stack
        # [-2, -2, -2, -3] minstack
        
        # stack = [2, 0, 3, 0]
        # minstack = [2,0,0,0]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack) == 0:
            self.minStack.append(x)
        elif x < self.minStack[-1]:
            self.minStack.append(x)
        else:
            curMin = self.minStack[-1]
            self.minStack.append(curMin)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minStack:
            self.minStack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]