# input n print out n number behinde it
import random

n = random.randint(1,100)
outputStream = ""


for i in range(n + 1):
    if i != 0:
        outputStream = outputStream + str(i)
print(outputStream)
print(n)
