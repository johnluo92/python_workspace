'''Balanced Brackets

Write a function that takes in a string made up of brackets and other optional characters. Return true if the brackets are complete sets without being out of ordered.

Valid sets:

{}
{[]}
(0(d))
'''

def balancedBrackets(string):
    # Write your code here.
    dic = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    myBrackets = []
    for i in string:
        print(myBrackets,i)
        if i in dic:
            myBrackets.append(i)
        else:
            if len(myBrackets) == 0:
                return False
            if i in dic.values():
                if i != dic[myBrackets.pop()]:
                    return False
    if len(myBrackets) > 0:
        return False
    return True  

string = "([])(){}(())()()"

print(balancedBrackets(string))