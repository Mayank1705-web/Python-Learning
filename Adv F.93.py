side1 = int(input("Enter first side of triangle: "))
side2 = int(input("Enter second side of triangle: "))
side3 = int(input("Enter third side of triangle: "))
if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
     print("The triangle is an isosceles triangle.")
else:
     print("The triangle is an scalene triangle.")