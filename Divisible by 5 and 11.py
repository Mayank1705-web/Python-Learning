num = int(input("Enter the number: "))
if num%5==0 and num%11==0:
    print("The number is divisible by 5 and 11")
elif num%5!=0 and num%11==0:
    print("The number is divisible by 11 but not by 5")
elif num%5==0 and num%11!=0:
    print("The number is divisible by 5 but not by 11")
else:
    print("The number is not divisible by 5 and 11")