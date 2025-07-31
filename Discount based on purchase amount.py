amount = float(input("Enter purchase amount: "))
if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0
print("Discount:", discount)
print("Final Amount:", amount - discount)
