for i in range(1, 6):
    for k in range(1, 6 - i):
        print(" ", end="")  
    for j in range(i):
        if j%2==0:
            print("1", end="")
        else:
            print("0", end="")
    print()
