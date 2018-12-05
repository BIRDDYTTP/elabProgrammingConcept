import math
def circle(radius):
    area = math.pi *radius*radius
    return area
def circumference(radius):
    cf = 2*math.pi*radius
    return cf
def sphere(radius):
    s = 4/3*math.pi*radius*radius*radius
    return s
r = float(input("Enter a radius: "))
print('Area of a circle with radius %.2f is %.2f.' % (r, circle(r)))
print('Circumference of a circle with radius %.2f is %.2f.' % (r, circumference(r)))
print('Volume of sphere with radius %.2f is %.2f.' % (r, sphere(r))