edge = 7
cube_volume = edge * edge * edge
cuboid_volume = 7 * 4 * 8
if cube_volume > cuboid_volume:
    shape = "Cube"
    diff = cube_volume - cuboid_volume
else:
    shape = "Cuboid"
    diff = cuboid_volume - cube_volume
print("19.", shape, "has more volume by", diff, "cm³")
