num = int(input("Enter a number: "))
sum_div = sum(i for i in range(1, num) if num % i == 0)
if sum_div == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
