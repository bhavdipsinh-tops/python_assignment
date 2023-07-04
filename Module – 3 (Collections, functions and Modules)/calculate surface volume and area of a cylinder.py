#Surface Area = 2 * π * r * (r + h)
#Volume = π * r^2 * h

import math

def calculate_cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume


radius = 7.5
height = 9.2

surface_area = calculate_cylinder_surface_area(radius, height)
volume = calculate_cylinder_volume(radius, height)

print(f"The surface area of the cylinder is: {surface_area:.2f}")
print(f"The volume of the cylinder is: {volume:.2f}")
