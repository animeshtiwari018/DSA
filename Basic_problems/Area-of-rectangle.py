def area_rectangle(length, width):
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = area_rectangle(length, width)

print("Area of Rectangle =", area)