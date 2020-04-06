from data import Data
import copy

data = Data(10, 0.1)
data.generate()
data.print()
data.encode()
data.print()
print(data.humm())
data.decode()
data.print()