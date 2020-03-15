import random

tab = []

def generate(dataSize):
    for i in range(0, dataSize):
        tab.append(random.randint(0,1))

def printData():
        print(tab)

