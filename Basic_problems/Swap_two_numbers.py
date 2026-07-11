def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


num1 = int(input("Enter the number"))
num2 = int(input("Enter the number"))


num1, num2 = swap(num1, num2)

print("After swapping:")
print("First number =", num1)
print("Second number =", num2)