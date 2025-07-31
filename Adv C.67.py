mark1 = float(input("Enter your marks for the first subject: "))
mark2 = float(input("Enter your marks for the second subject: "))
mark3 = float(input("Enter your marks for the third subject: "))
if 0 <= mark1 <= 100 and 0 <= mark2 <= 100 and 0 <= mark3 <= 100:
    print("All the entered marks are valid")
else: 
    print("anyone one of the entered marks is invalid")