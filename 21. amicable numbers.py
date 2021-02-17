def Divisors(x):
    list = [1]
    for i in range(2, x - 1):
        if x % i == 0:
            y = x / i
            list.append(y)
    return sum(list)

total = 0

for a in range(1, 10001):
    b = int(Divisors(a))
    y = int(Divisors(b))
    if a != b and y == a:
        total += a + b

print(total / 2)
