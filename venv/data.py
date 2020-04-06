import random
import copy


class Data:
    bits=[]              #lista z danymi
    dataSize = 0        #długość ciągu bitów
    hummPercentage = 0  #procentowa ilość błędów

    random.seed()
    def __init__(self,dataSize, hummPercentage):
        self.dataSize = dataSize
        self.hummPercentage = hummPercentage

    def generate(self):
        #generuje tablicę danych
        for i in range(0, self.dataSize):
            self.bits.append(random.getrandbits(1))

    # def hummm(self):
    #     for i in range(0, int(self.hummPercentage * self.dataSize)):
    #         temp = random.randrange(0, self.dataSize)
    #         self.bits[temp] = -self.bits[temp] + 1

    def humm(self):
        #zaszumia dane
        #TODO wybieranko zaszumiania

        #kopiuje tablicę do porównania
        temp = Data(self.dataSize, self.hummPercentage)
        temp.bits = copy.deepcopy(self.bits)
        counter = 0

        #zaszumianie
        for i in range(0, int(self.dataSize)):
            if(random.randrange(0,100)<=self.hummPercentage):
                self.bits[i] = -self.bits[i] + 1

        #obliczanie porcentu błędów
        for i in range(0, self.dataSize):
            if (temp.bits[i] != self.bits[i]):
                counter += 1
        return counter/self.dataSize

    def print(self):
        #printuje dane
        print(self.bits)

    #kodowanie za pomocą FEC
    def encode(self):
        encoded_bits = []
        for bit in self.bits:
            for i in range(0, 3):
                encoded_bits.append(bit)
        self.bits = encoded_bits
        self.dataSize *= 3

    def decode(self):
        decoded_bits = []
        zeros = 0
        ones = 0

        for bit in self.bits:
            zeros = 0
            ones = 0

            for i in range(0, 3):
                if bit == 0:
                    zeros += 1
                else:
                    ones += 1

            if zeros > ones:
                decoded_bits.append(1)
            else:
                decoded_bits.append(0)

        self.bits = decoded_bits
        self.dataSize /= 3