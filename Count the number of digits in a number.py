num = int(input("Enter a number: "))
count = 0
while num != 0: 
    a = num % 10
    count += 1
    num = num // 10
print("The number of digits is ", count)