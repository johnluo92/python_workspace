'''took me a sunday to really figure this one out.
Couldn't implement the code from the video as I dont
quite understand the solution fully, in addition I wanted
to implement a recursive DFS solution that utilizes stacks
to keep track of the managers of a node. Then comparing the 
two nodes's stacks to find the lowest common mananger.

The trick lies in the recursive function getManagers where we
do a DFS on the node and if that branch doesn't find it, the
call on that subtree will yield nothing. However, we still need
to keep going and so I used a tempstack to store the stack
where the stack will be overridden with none if that subtree 
doesnt find the node. Backtracking to the stack before the call,
removing the node we just did a DFS search on and continue onto
the next manager of the immediate manager we are exploring to
find this node.
'''

def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    stackOne = [topManager]
    stackTwo = [topManager]
    stackOne = getManagers(topManager, reportOne, stackOne)
    stackTwo = getManagers(topManager, reportTwo, stackTwo)
    while len(stackOne) < len(stackTwo):
        stackTwo.pop()
    while len(stackOne) > len(stackTwo):
        stackOne.pop()
    while len(stackOne):
        managerA = stackOne.pop()
        managerB = stackTwo.pop()
        if managerB != managerA:
            continue
        else:
            return managerA
                           
def getManagers(report, targetReport, stack):
    if not report.directReports and report != targetReport:
        return
    if report == targetReport:
        return stack
    if report.directReports:
        for sub in report.directReports:
            stack.append(sub.name)
            tempstack = stack
            stack = getManagers(sub, targetReport, stack)
            if stack:
                return stack
            else:
                tempstack.pop()
                stack = tempstack

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

#          A
#        /   \
#       B     C
#      / \   / \
#     D   E  F  G
#    / \
#   H   I

B = OrgChart('B')
C = OrgChart('C')
D = OrgChart('D')
E = OrgChart('E')
H = OrgChart('H')
I = OrgChart('I')
F = OrgChart('F')
G = OrgChart('G')

A = OrgChart('A')
A.directReports = [B, C]
B.directReports = [D, E]
D.directReports = [H, I]
C.directReports = [F, G]
ans = [A.name]
print(getManagers(A, I, ans))
ans = [A.name]
print(getManagers(A, E, ans))

print(getLowestCommonManager(A, E, I))
# ans = [A.name]
# print(getManagers(A, F, ans))