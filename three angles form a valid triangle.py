a1 = int(input("Enter First angle: "))
a2 = int(input("Enter Second angle: ")) 
a3 = int(input("Enter Third angle: "))
if a1+a2+a3 == 180 and a1>0 and a2>0 and a3>0:
    print("The angle are of a valid triangle")
else: 
    print("The angle are not of a valid triangle")