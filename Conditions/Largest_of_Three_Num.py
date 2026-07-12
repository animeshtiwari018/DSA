def Largest_of_3_Numbers(a, b, c):
    if a >= b and a >= c:
       print(a, "is the largest number")
    elif b >= a and b >= c: 
        print(b, "is the largest number")

    else: 
        print(c, "is the largest number")

        
num1 = int(input("Enter your numbers: "))
num2 = int(input("Enter your numbers: "))
num3 = int(input("Enter your numbers: "))


Largest_of_3_Numbers(num1, num2, num3)