import math
num = int(input("Enter a number: "))
if int(math.sqrt(num))**2 == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
