sub1 = float(input("Enter marks of first subject: "))
sub2 = float(input("Enter marks of second subject: "))
sub3 = float(input("Enter marks of third subject: "))
sub4 = float(input("Enter marks of fourth subject: "))
sub5 = float(input("Enter marks of fifth subject: "))
if sub1+sub2+sub3+sub4+sub5 >= 300:
    print("Total marks is > 300. Total marks= ", sub1+sub2+sub3+sub4+sub5)
else:
    print("Total marks is !> 300. Total marks= ", sub1+sub2+sub3+sub4+sub5)