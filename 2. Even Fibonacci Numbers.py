first = 1
second = 2
total = 0
evenSum = 0
while total < 4000000:
    if total > 4000000:
        break
    total = first + second
    first = second
    second = total
    print(total)
    if total % 2 == 0:
        evenSum = evenSum + total
print(evenSum)
