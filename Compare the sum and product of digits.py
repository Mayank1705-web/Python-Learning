num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
sum_digits = sum(digits)
product_digits = 1
for d in digits:
    product_digits *= d
if sum_digits > product_digits:
    print("Sum is greater")
elif product_digits > sum_digits:
    print("Product is greater")
else:
    print("Sum and Product are equal")
