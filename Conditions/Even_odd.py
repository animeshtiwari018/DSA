def even_odd(a):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
        
number = int(input("Enter a number: "))

result = even_odd(number)

print("The number is", result)