
from rectangle import Rectangle
from triangle import Triangle

rectangle = Rectangle()
print(rectangle)
triangle = Triangle()
print(triangle)

rectangle.set_values(30,40)
triangle.set_values(30,40)

print(rectangle.area())
print(triangle.area())