number = 600851475143

if number > 0:
    for i in range(number):
        if i != 0:
            if (number % i) == 0:
                number = number / i
                if i > 1:
                    for x in range (2, i):
                        if (i % x) == 0:
                            print('Not a prime number')
                        else:
                            print(i)
