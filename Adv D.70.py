sub1 = float(input("Enter marks of first subject: "))
sub2 = float(input("Enter marks of second subject: "))
sub3 = float(input("Enter marks of third subject: "))
if sub1 == sub2 and sub2 == sub3 and sub1 == sub3:
    print("All the subjects have same marks")
else:
    print("All the subjects have not same marks")