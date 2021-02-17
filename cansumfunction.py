def CanSum(targetSum, numbers, memo = {}):
    if (targetSum in memo): return memo[targetSum]
    if (targetSum == 0): return True
    if (targetSum < 0): return False

    #here are the two base cases, true if 0, false if below 0.
    for num in numbers:
        remainder = targetSum - num
        if (CanSum(remainder, numbers, memo) == True):
            memo[targetSum] = True
            return True


# here the false return is included after the recursive for loop to see if
# all possible answers are possible before false is called.
    memo[targetSum] = False
    return False


print(CanSum(345, [2, 6 ]))
print(CanSum(7, [2, 4]))
