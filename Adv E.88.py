last_day = 6
fine = 0
day = int(input("Enter the day at which the item is given: "))
if day <= 6:
    fine = 0
elif day > 6:
    fine = ((day - 6)*5)
else:
    fine = ((day - 6)*5)+(5*5)+(5*8)
print("The total fine is Rs.",fine)