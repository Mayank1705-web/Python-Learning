salary = int(input("Enter monthly salary: "))
age = int(input("Enter age: "))
if age >= 21 and age <= 60:
    if salary >= 25000:
        print("Eligible for Loan")
    else:
        print("Not Eligible due to low salary")
else:
    print("Not Eligible due to age")
