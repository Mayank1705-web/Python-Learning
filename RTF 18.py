num = int(input("Enter a number: "))
sum_digits = 0
product = 1
temp = num
while temp != 0:
    sum_digits += temp % 10
    product *= temp % 10
    temp //= 10
if product > sum_digits:
    print("Product is greater than sum")
else:
    print("Sum is greater than product")
