# Task 1: Calculate Factorial Using a Function
num = int(input("Enter an integer: "))

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"The factorial of {num} is: {factorial(num)}")
