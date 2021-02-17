
num = 1000
holder = 0
total = 0
for i in range(1000):
        holder = i
        if holder % 5 == 0:
            total = total + holder
        elif holder % 3 == 0:
            total = total + holder
print(total)
