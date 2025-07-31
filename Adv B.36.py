num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the second value: "))
if abs(num1) > abs(num2):
    print("The absolute value of ", num1," is greater than ", num2)
elif abs(num1) < abs(num2):
    print("The absolute value of ", num2," is greater than ", num1)
else:
    print("The absolute value of both the number is same.")