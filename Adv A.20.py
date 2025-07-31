import math
num = int(input("Enter a number: "))
root = int(math.sqrt(num))
if root * root == num: 
    print("The number is perfect square.")
else: 
    print("The number is not perfect square.")
