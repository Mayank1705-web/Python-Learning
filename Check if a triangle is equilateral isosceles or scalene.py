side1 = int(input("Enter the value of First side: "))
side2 = int(input("Enter the value of Second side: "))
side3 = int(input("Enter the value of Third side: "))
if side1==side2==side3:
    print("The triangle is an equilateral triangle")
elif side1==side2 or side2==side3 or side1==side3: 
    print("The triangle is an isosceles triangle")
else:
    print("The triangle is an scalene triangle")