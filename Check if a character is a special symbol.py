ch = input("Enter a character: ")
if not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9') or ch == ' '):
    print("Special Symbol")
else:
    print("Not a Special Symbol")
