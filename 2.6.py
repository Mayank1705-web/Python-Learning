a=10
b=9
perimeter=36
c = perimeter - a - b
s = perimeter / 2
temp = s*(s-a)*(s-b)*(s-c)
area = 1
i = 0
while i*i<=temp:
    area = i
    i+=1
print("Area of triangle: ",area,"cm^2")