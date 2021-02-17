import re
names = open('names.txt', 'r')
names = names.read()
names = [element.strip('"') for element in names.split(',')]

names.sort()
total = 0
listPos = 1
for name in names:
    sumHold = 0
    for letter in name:
        sumHold += ord(letter) - 64
    total += sumHold * listPos
    listPos += 1

print(total)
