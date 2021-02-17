
months = { 1 : '31', 2 : '28', 3: '31', 4 : '30', 5: '31', 6 : '30', 7 : '31', 8 : '31', 9 : '30', 10 : '31', 11 : '30', 12 : '31'}

month = 1
year = 1901
startDate = 6
sundayCount = 0
carry = 0
#all sundays are 7 days apart.

while year <= 2000:
    if year % 4 == 0 & month == 2:
        lenMonth = months[2] + 1
        #leap years in the month of february have one more day
    else:
        lenMonth = int(months[month])

    if year == 1901 & month == 1:
        lenMonth = lenMonth - startDate
        # starting off the calculations by finding the date with the first sunday in january
    lenMonth -= carry
    carry = lenMonth % 7
    # then doing a modulo of the remained by 7 to find when the first sunday of the next
    # month is.

    if carry == 1:
        sundayCount += 1
        month += 1
        # 1st of the month is a sunday. Add count.

    else:
        month += 1
        # otherwise increase the month count.

    if month > 12:
        month = 1
        year += 1
    else:
        month = month

print(sundayCount)
