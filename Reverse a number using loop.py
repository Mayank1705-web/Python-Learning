num = int(input("Enter a number: "))
while num != 0:
    a = num % 10
    print(a, end="")
    num //= 10