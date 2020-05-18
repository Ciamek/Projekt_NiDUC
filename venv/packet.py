import random

class Packet:
    random.seed()

    def __init__(self):
        self.bits = []

    def hum(self, hum_percentage):
        # zaszumia dane
        # TODO wybieranko zaszumiania

        # zaszumianie
        for i in range(0, len(self.bits)):
            if random.randrange(0, 100) <= hum_percentage:
                self.bits[i] = -self.bits[i] + 1

    def print(self):
        print(self.bits)

    # kodowanie za pomocą FEC
    # każdy bit zapisujemy n razy
    def fec_encode(self, n):
        encoded_bits = []
        for bit in self.bits:
            for i in range(0, n):
                encoded_bits.append(bit)
        self.bits = encoded_bits

    def fec_decode(self, n):
        decoded_bits = []
        ones = 0

        for i in range(0, len(self.bits), n):
            ones = 0

            for j in range(i, i + n):
                if self.bits[j] == 1:
                    ones += 1

            if ones > n / 2:
                decoded_bits.append(1)
            else:
                decoded_bits.append(0)

        self.bits = decoded_bits

    # zwraca liczbę bitów parzystości do wstawienia
    # def parity_bits(length):
    #    i = 1
    #    while i < length:
    #        i *= 2

    # def hamming_encode(self):
    #    length = len(self.bits)
    #    pos = 0