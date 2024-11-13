import math

def calculate_rectangle_area(length, width):
    return length * width
def calculate_circle_area(radius):
    return math.pi *radius ** 2
def calculate_triangle_area(base, height):
    return 1/2 * base *height
def calculate_area(shape, *dimensions):
    if shape == "rectangle":
        return calculate_rectangle_area(*dimensions)
    elif shape == "circle":
        return calculate_circle_area(*dimensions)
    elif shape == "triangle":
        return calculate_triangle_area(*dimensions)
shape = input("Enter the shape of the figure: ")
if shape == "rectangle":
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    print(f"The area of the rectangle is equal to {calculate_area('rectangle', length, width)}.")
elif shape == "circle":
    radius = int(input("Enter the radius of the circle: "))
    print(f"The area of the circle is equal to {calculate_area('circle', radius)}.")
elif shape == "triangle":
    base = int(input("Enter the length of the base of the triangle: "))
    height = int(input("Enter the length of the height of the triangle: "))
    print(f"The area of the triangle is equal to {calculate_area('triangle', base, height)}.")
else:
    print("Sorry, unknown figure:(")