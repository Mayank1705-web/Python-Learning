ch = input("Enter a character: ")
if ch.isalpha() and ord(ch) < ord('m'):
    print("The character is an alphabet and comes before 'm'.")
elif not ch.isalpha():
    print("The character is not an alphabet.")
else:
    print("The character is an alphabet but does not come before 'm'.")
