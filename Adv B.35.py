num = int(input("Enter a 2-Digit number: "))
f = num%10
l = num//10
if f == l:
    print("The first and the last digit of the number is same.")
else: 
    print("The first and the last digit of the number is not same.")