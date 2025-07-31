ch1 = input("Enter first character: ")
ch2 = input("Enter second character: ")
if ord(ch1) < ord(ch2):
    print(ch1," comes before ", ch2)
else: 
    print(ch2," comes before ", ch1)