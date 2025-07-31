amount = int(input("Enter the amount: "))
if amount >= 5000:
    print("20% discount, Total amount: ", amount-((amount*20)/100))
elif amount >= 3000:
    print("15% discount, Total amount: ",amount-((amount*15)/100))
elif amount >= 1000:
    print("10% discount, Total amount: ",amount-((amount*10)/100))
else:
    print("No discount")
