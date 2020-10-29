import random 

class gumball(object):
    def __init__(self, value, color):
        self.value = value
        self.color = color

class gumball_machine(object):
    def __init__(self):
        self.container = []

    def spit(self):
        gumba = random.choice(self.container)
        print(gumba.value, gumba.color)
        self.container.remove(gumba)
        return gumba
    
    def load(self, gumballobj):
        self.container.append(gumballobj)
        
#driver code:

my_gumball_machine = gumball_machine()
gumball1 = gumball('test1', 'testcolor')
my_gumball_machine.load(gumball('cotton candy', 'pink'))
my_gumball_machine.load(gumball('green apple', 'green'))
my_gumball_machine.load(gumball('strawberry', 'red'))

# print(my_gumball_machine.spit())

print(len(my_gumball_machine.container))
for i in my_gumball_machine.container:
    print(i.value, i.color)
    
print()

print(my_gumball_machine.spit())

print()
for i in my_gumball_machine.container:
    print(i.value, i.color)