from datetime import datetime
from generation import generation
from sorting import splitF

s = datetime.now()
generation()
t = datetime.now() - s
print("Generation took",t)
input("Press Enter to start sorting.")
s = datetime.now()
splitF()
t = datetime.now() - s
print("Sorting took",t)

