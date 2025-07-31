sub1 = float(input("Enter marks of first subject: "))
sub2 = float(input("Enter marks of second subject: "))
sub3 = float(input("Enter marks of third subject: "))
if (sub1 + sub2 + sub3) > 270:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")