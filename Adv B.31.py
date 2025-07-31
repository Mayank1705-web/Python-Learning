num = int(input("Enter a number: "))
sq = num **2
cube = num**3
if sq > cube:
    print("The square of the number is greater than cube of the number.")
elif cube > sq: 
    print("The square of the number is greater than cube of the number.")
else:
    print("The square of the number is equal to cube of the number.")