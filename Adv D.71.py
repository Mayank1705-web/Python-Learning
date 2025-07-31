sub1 = float(input("Enter marks of first subject: "))
sub2 = float(input("Enter marks of second subject: "))
sub3 = float(input("Enter marks of third subject: "))
if sub1 > sub2 and sub1 > sub3:
    print("The subject 1 has maximum marks") 
elif sub2 > sub3 and sub2 > sub1:
    print("The subject 2 has maximum marks")
else: 
     print("The subject 3 has maximum marks")