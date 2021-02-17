x = 1
for i in range(1, 101):
    x *= i
list = [int(y) for y in str(x)]
sum = 0
for i in list:
    sum += i
print(sum)
