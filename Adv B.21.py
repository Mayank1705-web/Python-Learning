num = int(input("Enter a number: "))
count = 0
while num != 0:
    num //= 10 
    count += 1
if count == 2:
    print("The number is a two-digit number.")
else: 
    print("The number is not a two-digit number.")