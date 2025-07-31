time = int(input("Enter the time in 24-hours formate: "))
if 0000 <= time < 1200:
    print("Its Morning time.")
elif 1200 <= time < 1700:
    print("Its Afternoon time.")
else: 
    print("Its Evening time.")