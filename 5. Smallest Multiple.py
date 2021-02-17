number = 20
i = 1
while i < 21:
    if number % i == 0:
        i += 1
        if i == 20 and number % i == 0:
            print(number)
    elif number % i != 0:
        number += 20
        i = 1
