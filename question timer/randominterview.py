class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.playerResponse = None

    def getRespose(self):
        if self.left:
            print(self.left.value)
        if self.right:
            print(self.right.value)

        self.playerResponse = input('get player response')