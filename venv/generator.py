import random

data = []



def generate(dataSize):
    for i in range(0, dataSize):
        data.append(random.randint(0,1))

def humm(percentage,dataSize):
    for i in range(0, int(percentage*dataSize)):
        temp = random.randrange(0, 100)
        data[temp]=-data[temp]+1


def printData():
    print(data)

