num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("The number is a positive even number.")
elif num < 0 and num % 2 == 0: 
    print("The number is a negative even number.")
elif num > 0 and num % 2 != 0:
    print("The number is a positive odd number.")
else:
    print("The number is a negative odd number.")