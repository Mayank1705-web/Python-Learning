income = float(input("Enter income: "))
if income <= 250000:
    print("No Tax")
elif income <= 500000:
    print("Tax: 5%")
elif income <= 1000000:
    print("Tax: 20%")
else:
    print("Tax: 30%")
