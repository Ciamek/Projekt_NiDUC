import random

class Data:
    tab=[]
    dataSize = 0
    hummPercentage = 0

    def __init__(self, dataSize, hummPercentage):
        self.dataSize = dataSize
        self.hummPercentage = hummPercentage

    def generate(self):
        for i in range(0, self.dataSize):
            self.tab.append(random.randint(0, 1))

    def humm(self):
        for i in range(0, int(self.hummPercentage * self.dataSize)):
            temp = random.randrange(0, 100)
            self.tab[temp] = -self.tab[temp] + 1

    def print(self):
        print(self.tab)

