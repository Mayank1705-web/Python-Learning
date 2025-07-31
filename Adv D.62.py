mark = float(input("Enter your marks: "))
if mark < 32:
    print("Grade: F")
elif 32 <= mark < 45:
    print("Grade: C")
elif 45 <= mark <= 55:
    print("Grade: B") 
else: 
    print("Grade: A")