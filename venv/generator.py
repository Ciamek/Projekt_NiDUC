import random

tab = []



def generate(dataSize):
    for i in range(0, dataSize):
        tab.append(random.randint(0,1))

def humm(percentage):
    for i in range(0, percentage*dataSize):
        temp = random.randrange(0, 100)
        tab[temp]=-tab[tamp]+1

def printData():
    print(tab)

