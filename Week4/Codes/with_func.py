# With Functions

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return 3.14 * radius**2

def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Calculate and print the area of different shapes
length = 5
width = 10
print("Area of rectangle:", calculate_rectangle_area(length, width))

radius = 3
print("Area of circle:", calculate_circle_area(radius))

base = 4
height = 8
print("Area of triangle:", calculate_triangle_area(base, height))
