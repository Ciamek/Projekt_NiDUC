from data import Data
import copy

data = Data(100000, 0.1)
data.generate()
data.print()
data.encode()
data.print()
print(data.humm())
