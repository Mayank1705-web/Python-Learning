l1 = 22
b1 = 15
area1 = l1 * b1
side2 = 21
area2 = side2 * side2
if area1 > area2:
    diff = area1 - area2
    bigger = "Shelly"
else:
    diff = area2 - area1
    bigger = "Rachel"
print("15.", bigger, "has bigger garden by", diff, "m²")
