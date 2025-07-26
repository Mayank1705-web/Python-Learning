math = int(input("Enter Math marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
total = math + physics + chemistry
mp_total = math + physics
if math >= 60 and physics >= 50 and chemistry >= 40:
    if total >= 200 or mp_total >= 150:
        print("Eligible for Admission")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")