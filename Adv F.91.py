side1 = int(input("Enter first side of the triangle: "))
side2 = int(input("Enter second side of the triangle: "))
side3 = int(input("Enter third side of the triangle: "))
if side1+side2 > side3 and side2+side3 > side1 and side1+side3 > side2:
    print("All the entered sides are of a valid triangle.")
else:
    print("All the entered sides are not of a valid triangle.")