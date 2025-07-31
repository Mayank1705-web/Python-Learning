temp = float(input("Enter your body temperature: "))
if temp < 36.1:
    print("You are having low body temperature.")
elif 36.1 <= temp < 37.2:
    print("You are having normal body temperature.")
else:
    print("You are having high body temperature.")