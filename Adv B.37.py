n1 = [1, 2, 3, 5]
print("The list is ", n1)
num = int(input("Enter a number to find in the list: "))
i = 0
while i < len(n1):
    if num == n1[i]:
        print("The number ", num," is in the list at ", i, "th index")
        break
    else: 
        print("The element is not in the list")
    i +=1
