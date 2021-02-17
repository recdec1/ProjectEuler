#This is a function of permutations

def factorial(x):
    if x == 1:
        return 1
    return x* factorial(x-1)

height = 5
width = 5
print(factorial(height + width)/(factorial(height)*factorial(width)))
