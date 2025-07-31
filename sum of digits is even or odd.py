num = int(input("Enter a number: "))
digit_sum = sum(int(d) for d in str(num))
if digit_sum % 2 == 0:
    print("Sum of digits is Even")
else:
    print("Sum of digits is Odd")
