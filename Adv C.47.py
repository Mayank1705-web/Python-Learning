ch = input("Enter a character: ")
if ch.isalnum() or ch.isnumeric() or ch.isdecimal() or ch.isalpha():
    print("The character is not special character.")
else:
    print("The character is special character.")