from data import Data
from packet import Packet
import copy

data = Data(2000, 3)

data.print()
print(data.transmit(5, "fec"))

data.print()
print(data.transmit(5, "hamming"))
data.print()