'''Min Max Stack Construction

Write a MinMaxStack class for a Min Max Stack. The class should support:

- pushing an popping values on and off the stack
- peeking at the value at the top of the stack
- getting both the minimum and maximum values in the stack at any given point in time

All methods, when considered independetly, should run in constant time and with constant space
'''

# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.maxstack = []
        
    def peek(self):
        # Write your code here.
        return self.stack[-1]
    
    def getMin(self):
        # Write your code here.
        return self.minstack[-1]

    def getMax(self):
        # Write your code here.
        return self.maxstack[-1]
    
    def push(self, number):
        if number == 7:
            print('max == > ', self.max)
        # Write your code here.
        if self.stack == []:
            self.min = number
            self.max = number
            self.minstack.append(number)
            self.maxstack.append(number)
        elif number < self.minstack[-1]:
            self.minstack.append(number)
        elif number >= self.maxstack[-1]:
            self.maxstack.append(number)
        self.stack.append(number)
    
    def pop(self):
        # Write your code here.
        if self.stack[-1] == self.maxstack[-1]:
            self.maxstack.pop()
        elif self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

