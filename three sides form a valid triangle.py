side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))
if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    print("Print the sides are of a valid triangle")
else:
    print("Print the sides are not of a valid triangle")