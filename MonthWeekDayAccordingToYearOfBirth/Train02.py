year = input("Enter your Year of Birth: ")

yearLen = len(year)

if yearLen != 4:
    raise TypeError("Year of birth must be 4 digits")
else:
    yearInt = int(year)

month = yearInt * 12
week = month * 4
day = week * 7

print("Year: %s | Month: %s | Week: %s | Day: %s" % (yearInt, month, week, day))