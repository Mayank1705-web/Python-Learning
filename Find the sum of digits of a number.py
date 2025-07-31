num = int(input("Enter a number: "))
sum = 0
while num != 0:
    a = num % 10
    sum += a
    num //= 10
print("The sum of the digits of the number is ", sum)