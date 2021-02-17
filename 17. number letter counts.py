#numbers with single digits will be used 9 times for every 100 numbers.
#ie, 1 is used in 1, 21, 31, 41 ,51 ,61 71, 81, 91
#the numbers above 10 should be considered as used once per every 100 numbers.
# ie, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen,
# nineteen,

# once, the hundreds are reached, the word hundred must be considered in every
# word addition; then 'and' must be used in every number that isnt base 100.


numbersDict = { 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thriteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety', 100 : 'hundred', 'and' : 'and', 1000 : 'thousand'}

# quick maths
# 1 is used 9 times per 100, so 90 times per 1000. then 100 times for 100 - 199, then add 1 more occasion for 1000. total of 191 times
# ^^ this is the same for 1 through 9. All numbers are used that many times.

# the values in the 10s are then used 1 times for every 100. so 10 times per 1000.

# the hundred is used 899 times

# the and is used 890 times

# the thousand is used once.

countTotal = 0

for x in range(1, 1001):
    if len(str(x)) == 1:
        countTotal += len(numbersDict[x])
    if len(str(x)) == 2:
        list =

print(countTotal)
