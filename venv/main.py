from data import Data
from packet import Packet
import copy

data = Data(10, 20)

data.print()
print(data.transmit(5, "fec"))

