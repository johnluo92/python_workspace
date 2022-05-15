def sortStack(stack):
    # Write your code here.
    sortStack(stack, stack.pop())
    return stack

def sortStack(stack, top):
    if len(stack) == 1:
        if top < stack[-1]:
            temp = stack.pop()
            stack.append(top)
            stack.append(temp)
            return True
        else:
            stack.append(top)
        return
    
    switched = True
    
    while switched:
        switched = False
        sortedStack(stack, top)
        