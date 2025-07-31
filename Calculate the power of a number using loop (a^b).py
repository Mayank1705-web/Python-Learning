num = int(input("Enter a number: "))
power = int(input("Enter a the degree to with the number is to be exponetially increased: "))
value = num
for i in range (1, power):
    value *= num 
print(num, " to the power ", power, " is ", value)