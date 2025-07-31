hypotenuse = 13
side1 = 12
side2 = (hypotenuse * hypotenuse) - (side1 * side1)
for i in range(side1):
    if i * i == side2:
        other_side = i
        break
area = (side1 * other_side) // 2
print("Other side:", other_side, "cm, Area:", area, "cm²")
