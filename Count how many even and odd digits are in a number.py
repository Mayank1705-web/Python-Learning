num = int(input("Enter a number: "))
temp = num
while num != 0:
    a = num % 10
    if a % 2 == 0:
        print(a, " is an even digit in the number ", temp)
    else: 
        print(a, " is an odd digit in the number ", temp)
    num //= 10