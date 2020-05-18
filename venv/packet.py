import random
import math

class Packet:
    random.seed()

    def __init__(self):
        self.bits = []

    def hum(self, hum_percentage):
        # TODO wybieranko zaszumiania

        # zaszumianie
        for i in range(0, len(self.bits)):
            if random.randrange(0, 100) <= hum_percentage:
                self.bits[i] = -self.bits[i] + 1

    def print(self):
        print(self.bits)

    # Kodowanie za pomocą FEC.
    # Każdy bit zapisujemy n razy.
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


    #@staticmethod
    #def get_2s_powers_range(n):
    #    return [1 << i for i in range(int(math.log2(n+1)))]

    @staticmethod
    def get_2s_powers_range(n):
        powers = []
        i = 1
        while i < n:
            powers.append(i)
            n += 1
            i = i << 1
        return powers

    def hamming_encode(self):

        # [1, 2, 4, 8, ... < n]
        powers = self.get_2s_powers_range(len(self.bits))

        # Na pozycjach będących kolejnymi potęgami dwójki wstawiamy bity parzystosci.
        for p in powers:
            self.bits.insert(p-1, 0)

        # Obliczamy bity parzystosci.
        for p in powers:
            sum = 0
            for i in range(p-1, len(self.bits), 2*p):
                # Obliczamy sumę p kolejnych bitów.
                sum += self.bits[i : i + p].count(1)
            self.bits[p-1] = 1 if sum % 2 else 0