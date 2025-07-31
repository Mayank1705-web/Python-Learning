age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
min_age = 18
max_age = 30
min_height = 160
if min_age <= age <= max_age and height >= min_height:
    print("You qualify for the sports team!")
else:
    print("You do not qualify for the sports team.")
