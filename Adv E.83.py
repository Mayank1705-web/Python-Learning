age1 = int(input("Enter the age of first person: "))
age2 = int(input("Enter the age of second person: "))
if age1 > age2:
    print("The age of first person is elder than second person.")
elif age2 > age1:
    print("The age of the second person is elder than first person.")
else:
    print("The age of both the person are equal.")