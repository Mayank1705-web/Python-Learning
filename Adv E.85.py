age = int(input("Enter your age: "))
health = True
if 18 <= age <= 60 and health == True:
    print("Eligible for insurance")
else:
    print("Not eligible for insurance")