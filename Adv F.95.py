num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 < num2 and num1 > num3:
    print("The middle number is ", num1)
elif num2 < num3 and num2 > num1:
    print("The middle number is ", num2)
else: 
    print("The middle number is ", num3)