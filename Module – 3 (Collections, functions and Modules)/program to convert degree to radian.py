import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians


degrees = 180

radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is equal to {radians:.2f} radians.")
