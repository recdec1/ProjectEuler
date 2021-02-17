total = 0
largest = 0
for x in range(1000):
    for y in range(1000):
        total = x * y
        string = str(total)
        forward = []
        backward = []
        for i in string:
            forward.append(i)
            backward.insert(0, i)
        if forward == backward:
            strnumber = [str(v) for v in forward]
            a_number = "".join(strnumber)
            number = int(a_number)
            if number > largest:
                largest = number
print(largest)
