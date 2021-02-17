import math


def check_prime(num):
    if num > 2 and num % 2 == 0:
        return False
    else:
        # I tried using a generator here,
        # but it is slower by a noticeable amount.
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
    return True


def find_sum(limit):
    sum = 0
    for i in range(2, limit):
        if check_prime(i):
            sum += i

    return sum


if __name__ == '__main__':

    # Find the sum of all primes below two million
    print(find_sum(2000000))

    # confirm above is correct by solving example
    # and verifying results are euqal to that presented
    # by example
    print(find_sum(10))
