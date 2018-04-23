import sys
import os

sys.path.append(os.path.realpath(".."))

[print(p, '\n') for p in sys.path]
