import random
import copy


class Data:
                 #lista z danymi
    random.seed()
    def __init__(self, dataSize, hummPercentage, packetSize, n):
        self.bits = []
        self.dataSize = dataSize
        self.hummPercentage = hummPercentage
        self.packetSize = packetSize
        self.packet = self.Packet( hummPercentage, n)
        self.generate()

    def generate(self):
        #generuje tablicę danych
        for i in range(0, self.dataSize):
            self.bits.append(random.getrandbits(1))

    def print(self):
        # printuje dane
        print(self.bits)

    #funkcja symulująca transmisję, zwraca procentową liczbę błędów
    def transmit(self):
        transmitedData = []
        counter = 0

        for i in range(0, self.dataSize, self.packetSize):
            self.packet.bits = self.bits [i:i+self.packetSize]
            #dopisuje 0 jeśli brakuje bitów do pakitu
            while (self.packet.bits.__len__()<self.packetSize):
                self.packet.bits.append(0)

            self.packet.encode()
            self.packet.humm()
            self.packet.decode()

            #dołącza pakiet do listy bitów
            for j in range (0, self.packetSize):
                transmitedData.append(self.packet.bits[j])
        #oblicza ilość błędów
        for i in range (0, self.bits.__len__()):
            if(transmitedData[i] != self.bits[i]):
                counter += 1

        return counter/self.bits.__len__()


    class Packet:
        random.seed()
        def __init__(self, hummPercentage, n):
            self.bits = []
            self.hummPercentage = hummPercentage
            self.n = n

        def humm(self):
            #zaszumia dane
            #TODO wybieranko zaszumiania

            #kopiuje listę do porównania
            tempBits = self.bits
            counter = 0

            #zaszumianie
            for i in range(0, int(self.bits.__len__())):
                if(random.randrange(0,100)<=self.hummPercentage):
                    self.bits[i] = -self.bits[i] + 1

        def print(self):
            # printuje dane
            print(self.bits)

        #kodowanie za pomocą FEC
        def encode(self):
            encoded_bits = []
            for bit in self.bits:
                for i in range(0, self.n):
                    encoded_bits.append(bit)
            self.bits = encoded_bits


        def decode(self):
            decoded_bits = []
            zeros = 0
            ones = 0

            for i in range(0, self.bits.__len__(), self.n):
                zeros = 0
                ones = 0

                for j in range(i, i+self.n):
                    if self.bits[j] == 0:
                        zeros += 1
                    else:
                        ones += 1

                if zeros > ones:
                    decoded_bits.append(0)
                else:
                    decoded_bits.append(1)
            self.bits = decoded_bits



#zaszumianie
#drugi algorytm
#podział na pakiety

#2 etap:
# statystyki - srednia i odchylenie, na 3
# 5 nr summary 5 kwantyli rozkładu wykresik, na 4
# dopasowywanie funkcji do danych (fitting function to data) histogram - rozkład Gaussa, excel/R/python/gnuplot-fitGauss, zwrócić mi i sigma i wykresik, wystarczy mi i sigma, na 5