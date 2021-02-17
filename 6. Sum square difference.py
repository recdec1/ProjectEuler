sqTotal = 0
sqSum = 0
for i in range(101):
    sqTotal = sqTotal + i ** 2
for x in range(101):
    sqSum = sqSum + x
sqSum = sqSum ** 2
total = sqSum - sqTotal
print(total)
