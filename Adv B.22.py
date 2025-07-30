num  = int(input("Enter a number: "))
count = 0 
while num != 0:
    num //= 10
    count += 1
if count == 3:
    print("The number is a three - digit number.")
else: 
    print("The number is not a three - digit number.")
