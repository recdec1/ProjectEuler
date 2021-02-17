largest = 0
value = 0
for i in range(2, 1000001):
    number = i
    counter = 1
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            counter += 1
        elif number % 2 != 0:
            number = (number * 3) + 1
            counter += 1
    if counter > largest:
        largest = counter
        value = i
#  to account for the final number 1
print(value)
