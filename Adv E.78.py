age = int(input("Enter the age of person: "))
if age < 18:
    print("The person is minor")
elif 18 <= age < 60:
    print("The person is adult")
else:
    print("The person is senior citizen")