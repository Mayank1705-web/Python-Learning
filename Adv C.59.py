ch1 = input("Enter first character: ")
ch2 = input("Enter second character: ")
if ord(ch1) == ord(ch2)+1:
    print("The character ", ch1," is after ", ch2)
elif ord(ch2) == ord(ch1)+1:
    print("The character ", ch2," is after ", ch1)
else: 
    print("The character are not after one another")