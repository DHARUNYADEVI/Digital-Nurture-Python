import math
def circle_area(radius):
    if radius<=0:
        print("Invalid radius")
        return
    area=math.pi*radius**2
    print(f"Area of the circle: {area:.2f}")
circle_area(5)    