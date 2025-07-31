angle1 = int(input("Enter first angle of the triangle: "))
angle2 = int(input("Enter second angle of the triangle: "))
angle3 = int(input("Enter third angle of the triangle: "))
if angle1 + angle2 + angle3 == 180:
    print("All the angles are of valid triangle")
else:
    print("All the angles are not of valid triangle")