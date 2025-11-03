from graphics.rectangle import area as rect_area
from graphics.circle import area as circle_area
from graphics.three_d_graphics.cuboid import surface_area as cuboid_area
from graphics.three_d_graphics.sphere import surface_area as sphere_area
print("Rectangle area:", rect_area(10, 5))
print("Circle area:", circle_area(7))
print("Cuboid surface area:", cuboid_area(3, 4, 5))
print("Sphere surface area:", sphere_area(6))
