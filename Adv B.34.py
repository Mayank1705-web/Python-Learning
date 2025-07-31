num = int(input("Enter a number: "))
f = 0
if num == 5:
    f += 1
else: 
    while num != 0:
        num %= 10
        if num == 5:
            f += 1
            break
        num /= 10
if f==1:
    print("The last digit of the number is 5")
else:
    print("The last digit of the number is not 5")