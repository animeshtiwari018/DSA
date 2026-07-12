def largest_of_2_num(a, b):
    if a > b:
        print(a, "is larger")
    elif b > a:
        print(b, "is larger")
    else:
        print("Both numbers are equal")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest_of_2_num(a, b)