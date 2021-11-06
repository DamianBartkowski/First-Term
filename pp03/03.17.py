plane_x = int(input("X cords:"))
plane_y = int(input("Y cords:"))
p = [plane_x,plane_y]
print("X:", plane_x)
print("Y:", plane_y)
if plane_x > 0 and plane_y > 0:
    print("Point P:",p, "is in the first quadrant of the coordinate system")
if plane_x < 0 and plane_y > 0:
    print("Point P:",p, "is in the second quadrant of the coordinate system")
if plane_x < 0 and plane_y < 0:
    print("Point P:",p, "is in the third quadrant of the coordinate system")
if plane_x > 0 and plane_y < 0:
    print("Point P:",p, "is in the fourth quadrant of the coordinate system.")
if plane_x == 0 and plane_y == 0:
    print("Point P:", p, "is in the centre of the coordinate system.")
elif plane_x == 0:
    print("Point P:", p, "is in the X axis.")
else:
        print("Point P:", p, "is in the Y axis.")
