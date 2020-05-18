from data import Data
from packet import Packet
import copy

data = Data(10, 20)

data.print()
print(data.transmit(5, "fec"))

packet = Packet()
packet.bits = [0, 1, 1, 0, 0, 1]
packet.print()
packet.hamming_encode()
packet.print()