num = int(input("Enter a number: "))
if num % 6 == 0 and num > 50:
    print("The number is divisible by 6 and greater than 50")
elif num % 6 == 0 and num < 50: 
    print("The number is divisible by 6 and less than 50")
elif num % 6 != 0 and num > 50: 
    print("The number is not divisible by 6 and greater than 50")
else: 
    print("The number is not divisible by 6 and less than 50")