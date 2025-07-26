target_area = 149
height = 6
for r in range(1, 50):
    surface = 2 * pi * r * r + 2 * pi * r * height
    if int(surface) == target_area:
        diameter = 2 * r
        break
print("37. Diameter is:", diameter, "cm")