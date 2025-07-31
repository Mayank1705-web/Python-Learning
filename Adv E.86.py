date = int(input("Enter a date: "))
month = int(input("Enter a month: "))
if 1 <= date <= 31 and 1 <= month <= 12:
    print("The entered date is a valid date.")
else: 
    print("The entered date is not a valid date.")