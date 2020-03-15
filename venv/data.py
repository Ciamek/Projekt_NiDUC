import random
import copy


class Data:
    tab=[]              #tablica z danymi
    dataSize = 0        #długość ciągu bitów
    hummPercentage = 0  #procentowa ilość błędów

    random.seed()
    def __init__(self, dataSize, hummPercentage):
        self.dataSize = dataSize
        self.hummPercentage = hummPercentage

    def generate(self):
        #generuje tablicę danych
        for i in range(0, self.dataSize):
            self.tab.append(random.getrandbits(1))

    # def hummm(self):
    #     for i in range(0, int(self.hummPercentage * self.dataSize)):
    #         temp = random.randrange(0, self.dataSize)
    #         self.tab[temp] = -self.tab[temp] + 1

    def humm(self):
        #zaszumia dane
        #TODO wybieranko zaszumiania

        #kopiuje tablicę do porównania
        temp = Data(self.dataSize, self.hummPercentage)
        temp.tab = copy.deepcopy(self.tab)
        counter = 0

        #zaszumianie
        for i in range(0, int(self.dataSize)):
            if(random.randrange(0,100)<=self.hummPercentage):
                self.tab[i] = -self.tab[i] + 1

        #obliczanie porcentu błędów
        for i in range(0, self.dataSize):
            if (temp.tab[i] != self.tab[i]):
                counter += 1
        return counter/self.dataSize

    def print(self):
        #printuje dane
        print(self.tab)

