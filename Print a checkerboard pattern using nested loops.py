for i in range (1, 6):
    for j in range (1,6):
        if j % 2 != 0 :
            print("*", end= "")
        elif i % 2 == 0:
            print("|", end= "")
        else: 
            print("-", end= "")
    print()