number = 2 ** 1000

list = [int(x) for x in str(number)]
sum = 0
for i in list:
    sum = sum + i

print(sum)
