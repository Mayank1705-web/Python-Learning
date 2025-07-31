num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("---OPERATORS---\n + for Addition\n - for Substraction\n * for Multiplication\n / for Division")
operator = input("Enter an operator: ")
if operator == '+' or operator == '-' or operator == '*' or operator == '/': 
    match operator:
        case '+':
            print("The addition of two numbers is ", num1 + num2)
        case '-':
            print("The substraction of two numbers is ", num1 - num2)
        case '*':
            print("The multiplication of two numbers is ", num1 * num2)
        case '/':
            print("The division of two numbers is ", num1 / num2)
else: 
    print("Invalid operator used.")