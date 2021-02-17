import math
total = 0

for i in range(1, 1001):
    total += pow(i, i)

total = str(total)
print(total[-10:])
