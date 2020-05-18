import random
from packet import Packet

class Data:

    random.seed()
    def __init__(self, size, hum_percentage):
        self.bits = []
        self.size = size
        self.humPercentage = hum_percentage
        self.generate()

    def generate(self):
        for i in range(0, self.size):
            self.bits.append(random.getrandbits(1))

    def print(self):
        print(self.bits)

    #funkcja symulująca transmisję, zwraca procentową liczbę błędów
    def transmit(self, packet_size, encoding):
        data_received = []
        packet = Packet()

        for i in range(0, self.size, packet_size):
            packet.bits = self.bits [i:i+self.size]

            #dopisuje 0 jeśli brakuje bitów do pakietu
            while len(packet.bits) < self.size:
                packet.bits.append(0)

            # kodowanie
            if encoding == "fec":
                packet.fec_encode(3)
            elif encoding == "hamming":
                packet.hamming_encode()
            #

            packet.hum(self.humPercentage)

            # dekodowanie
            if encoding == "fec":
                packet.fec_decode(3)
            elif encoding == "hamming":
                packet.hamming_decode()
            #

            #dołącza pakiet do bitów odebranych
            for j in range (0, packet_size):
                data_received.append(packet.bits[j])

        #oblicza ilość błędów
        errors = 0
        for i in range (0, len(self.bits) - 1):
            if data_received[i] != self.bits[i]:
                errors += 1
        #

        if len(self.bits) == 0:
            return 0;
        else:
            return errors/len(self.bits)

#zaszumianie
#drugi algorytm
#podział na pakiety

#2 etap:
# statystyki - srednia i odchylenie, na 3
# 5 nr summary 5 kwantyli rozkładu wykresik, na 4
# dopasowywanie funkcji do danych (fitting function to data) histogram - rozkład Gaussa, excel/R/python/gnuplot-fitGauss, zwrócić mi i sigma i wykresik, wystarczy mi i sigma, na 5