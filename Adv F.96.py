rec1_length = int(input("Enter the length of rectangle 1: "))
rec1_breath = int(input("Enter the breath of rectangle 1: "))
rec2_length = int(input("Enter the length of rectangle 2: "))
rec2_breath = int(input("Enter the breath of rectangle 2: "))
if rec1_length * rec1_breath > rec2_length * rec2_breath:
    print("The area of first triangle is more than second triangle.")
elif rec1_length * rec1_breath < rec2_length * rec2_breath:
    print("The area of second triangle is more than first triangle.")
else:
    print("The area of both the triangles are equal.")
