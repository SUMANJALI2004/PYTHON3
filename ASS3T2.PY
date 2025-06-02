# Task 2: Using the Math Module for Calculations

import math
num = float(input("Enter a number: "))

sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)  # Input is in radians

print(f"Square root of {num} is: {sqrt_val}")
print(f"Natural logarithm of {num} is: {log_val}")
print(f"Sine of {num} (in radians) is: {sine_val}")
