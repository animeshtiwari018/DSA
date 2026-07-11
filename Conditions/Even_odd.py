def even_odd():
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
        
number = int(input("Enter a number: "))

result = even_odd(number)

print("The number is", result)