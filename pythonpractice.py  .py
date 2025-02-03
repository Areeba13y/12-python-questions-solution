# CODE 1
# Simple program to print "Hello, World!"
print("Hello, World!")

# CODE 2
# Program to perform arithmetic operations on two numbers
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
sum_result = num1 + num2
print("Sum of num1 and num2 is:", sum_result)

# CODE 3
# Program to perform division of two numbers
num3 = float(input("Enter first number: "))
num4 = float(input("Enter second number: "))
if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    d_result = num3 / num4
    print("Division of num3 and num4 is:", d_result)

# CODE 4
# Program to find the area of a triangle
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
area = 0.5 * base * height
print("Area of the triangle is:", area)

# CODE 5
# Program to swap two variables using a temporary variable
a = input("Enter first value: ")
b = input("Enter second value: ")
print(f"Original values: a={a}, b={b}")
temp = a
a = b
b = temp
print(f"After swapping: a={a}, b={b}")

# CODE 6
# Program to generate a random number
import random
print(f"Random number: {random.randint(1, 70)}")

# CODE 7
# Program to convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# CODE 8
# Program to convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")

# CODE 9
# Program to display a calendar of a given month and year
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)

# CODE 10
# Program to swap two variables without using a temporary variable
a = input("Enter first value: ")
b = input("Enter second value: ")
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)

# CODE 11
# Program to check if a number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# CODE 12
# Program to check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
