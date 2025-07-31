marks1 = float(input("Enter the marks of the first subject: "))
marks2 = float(input("Enter the marks of the second subject: "))
if marks1 > marks2:
    print("Marks of first subject is greater than second subject.")
elif marks1 < marks2:
    print("Marks of second subject is greater than first subject.")
else:
    print("Marks of both the subjects are equal.")