def simple_interest(principal, rate, time):
    return principal * rate * time

# 1. Get input from the user and convert to numbers
# Use float() for money and rates since they often have decimals
p = float(input("Enter the principal amount: "))
r = float(float(input("Enter the interest rate (as a decimal, e.g., 0.05 for 5%): ")))
t = float(input("Enter the time in years: "))

# 2. Call the function and calculate the result
result = simple_interest(p, r, t)

# 3. Print the final answer
print(f"The simple interest is: {result}")
