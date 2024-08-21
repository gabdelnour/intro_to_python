# -*- coding: utf-8 -*-
"""Intro_to_Programming_with_Python 1 _Notebook

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BnSw4Uhym4tEO_Gm7XEklnJeEev9-fw2

# Basics of Python

`print()` is a function in python which takes a string and will print the content on the console.

We also have comments which can be used in Python, whatever is represented as comments will never be processed by Python.

Remember, comments are essential for making your code readable and understandable, especially for yourself and others who may read your code in the future. Use them to explain your thought process, document important details, and clarify complex parts of your code.
"""

"""
This is a multi-
line comment using triple quotes
and this will never be executed by python.
"""

# Also this is a single-line comment

print("This will be printed on the console")

print("Hello") # This is an in-line comment

"""# Variables & Data Types


"""

name = "Alice" # String data type

age = 18 # integer data type

has_license = True # boolean data type

cgpa = 3.8 # float data type

print(name)
print("Current age:", age)

# Creating / modifying variables

updated_age = age + 5

print("New updated age:", updated_age)

print(type(age))

print(type(name))

print(type(has_license))

print(type(cgpa))

"""We can declare strings using single quotes or double quotes. Also below are examples which will show how you can use a single quote or double quote or both inside a string. If you want to use any of the quote inside the string you can always use `\` which is called an escape character which will escape the `"` or `'`. Below are the examples:"""

greeting_double_quotes = "She said, 'Hello, World!'"

greeting_single_quotes = 'He said, "Hello, World!"'

greeting_escape_character = "She said, \"Hello, World!\" from \'Python\'"

print(greeting_double_quotes)

print(greeting_single_quotes)

print(greeting_escape_character)

"""# Arithmetic Operators

We will perform all the arithmetic operations available in python and see the results. Below are all the operations.

We will consider two variables `a` and `b`. For each operation we will create a new variable to store the result and print it at the end.

You can also observe that floor division and divison operation gives `int` and `float` values respectively.
"""

a = 10

b = 4

addition = a + b # Adding of 2 numbers

subtraction = a - b # Subtracting of 2 numbers

multiplication = a * b # Multiplication of 2 numbers

division = a / b # Division of 2 numbers

floor_division = a // b # Integer part of the division operation

remainder = a % b # returns the remainder of the division operation

power = a ** b # returns by performing a to the power of b


print("addition of a and b is:", addition)

print("subtraction of a and b is:", subtraction)

print("multiplication of a and b is:", multiplication)

print("division of a and b is:", division)

print("floor_division of a and b is:", floor_division)

print("remainder of a and b is:", remainder)

print("power of a and b is:", power)

print("type of division result:", type(division)) # Python implicitly converts it to float type for division operation

"""# Assignment Operators

Assignment operators in Python are used to assign values to variables. They combine an operation with assignment.

We can use any arithmetic operator followed by `=` which makes it in-place assignment operation, For example: `+=` adds the right operand to the left operand and assigns the result to the left operand. It is a shorthand notation for updating the value of a variable by adding another value to it. Below are the examples:
"""

# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b = b + 10  # 20


#Use += to add 10 to the existing value of b
b += 10  # b = b + 10

print(b)

b /= 10 #option 1
b = b / 10 #option 2

# Subtract and assign value
b -= a  # b = b - a
print(b)

# multiply and assign
b *= a
b = b * a
print(b)

"""# Comparison Operators

Comparison operators in Python are used to compare values and expressions, and they return a Boolean result (True or False). These operators play a crucial role in controlling the flow of a program, making decisions based on conditions, and expressing relationships between different values.
"""

a = 20
b = 30

# a > b is False

x = a > b # False
print(x)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)

"""# Logical Operators"""

a = True
b = False



# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)

print(not b)

a = True
b = False

c = a or b # || in other languagaes
d = a and b  # && in other languages

a += 1

print(c)
print(d)

"""# If Else Statements

The below code is to find whether the given number is even or odd using conditional statements
"""

a = 12

# if-else
if a % 2 == 0:
    print("Hey its even")
else:
    print("Hey its odd")
print("It might be even or odd, I will always be executed")

"""The below code is find the grade of a student from the score."""

# if else statements to find the Grade of a student based on the exam score

score = 91

# Check the grade based on the score
if score >= 90:
    # Grade A: If the score is 90 or above
    print("Grade: A")
elif score >= 80:
    # Grade B: If the score is between 80 and 89
    print("Grade: B")
elif score >= 70:
    # Grade C: If the score is between 70 and 79
    print("Grade: C")
elif score >= 60:
    # Grade D: If the score is between 60 and 69
    print("Grade: D")
else:
    # Grade F: If the score is below 60
    print("Grade: F (Fail)")

"""The below code is find out whether the given number is positive, negative or zero."""

number = 1

# if-elif-else
if number > 0:
   print("Positive number")
   print("Inside if block")

elif number < 0:
    print("-ve number")
    print("Inside if else")

else:
    print("Zero")
    print("Inside else")

"""The below code is to find out what traingle type it is given the length of all 3 sides of a traingle"""

# Triangle type example based on sides
side1 = 10
side2 = 10
side3 = 10

# Check triangle type
if side1 == side2 == side3:
    print("Equilateral Triangle: All sides are equal.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles Triangle: Two sides are equal.")
else:
    print("Scalene Triangle: No sides are equal.")

"""The below code takes 3 values and checks whether they form a Pythagorean Triplet or not."""

# Pythagorean triplet example
a = 3
b = 4
c = 5

# Check if it forms a Pythagorean triplet
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("The numbers form a Pythagorean triplet.")
else:
    print("The numbers do not form a Pythagorean triplet.")

"""A simple calculator which takes input from the user to perform the desired calculation. You might not know `input()`  function and wonder how it works don't worry that will be covered in the coming slides. For now consider it as blackbox which allows you to take input from the user.

The below python program based on the choice you have provided performs either of the following operations.
1. Addition
2. Subtraction
3. Multiplication
4. Division
"""

# This is a simple calculator using if-else statements and input() function.

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# take input from the user
choice = input("Enter choice(1/2/3/4): ")

# check if choice is one of the four options
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == '4':
        print(num1, "/", num2, "=", num1 / num2)

# nested if-else

a = 9

if a % 2 == 0:
    if a % 5 == 0:
        print("It is even and also divisible by 5")
    elif a % 6 == 0:
        print("it is even and also divisible by 6")
    else:
        print("it is an even number, not divisible by 5 and 6")
else:
    if a % 3 == 0:
        print("it is odd and also divisible by 3")
    else:
        print("It is odd but not divisible by 3")

"""# Loops"""

for i in range(10): # for (int i=0; i<10; i++)
    print("Hello world")
    print(i)

for i in range(10, 20): # for (i=10; i<20; i++)
    print(i)


print("")
for i in range(0, 20, 3): # for (i=1; i<20; i = i+2)
    print(i)

# while loop

i = 0
while i < 10:
    print(i)
    i += 1

"""Program to Check Whether a Number is Prime or not"""

# program tells whether the given number is a prime number or not.


# Take user input
user_input = int(input("Enter a number: "))
flag = True

if user_input <= 1:
    flag = False
elif user_input == 2:
    flag = True
elif user_input % 2 == 0:
    flag = False
else:
    # Check for factors from 3 to the square root of the number
    for i in range(3, int(user_input**0.5) + 1, 2):
      if user_input % i == 0:
        flag = False
        break

if flag:
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")

"""A Python program which finds whether a given number is Armstrong number.

An Armstrong number (also known as a narcissistic number, pluperfect digital invariant, or pluperfect number) is a number that is the sum of its own digits each raised to the power of the number of digits.
Ex: 153 -> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

Sharing 2 different solutions to solve the same problem.
"""

# Solution 1: Python program to check if the number is an Armstrong number or not

# take input from the user
num_str = input("Enter a number: ")
num = int(num_str)
n = len(num_str)
# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

"""Python program to find numbers that are divisible by 7 but not by 5 in the range from 2000 to 3500"""

# Initialize an empty list to store the result
result_numbers = []

# Loop through the range 2000 to 3500 (inclusive)
for num in range(2000, 3501):
    # Check if the number is divisible by 7 and not divisible by 5
    if num % 7 == 0 and num % 5 != 0:
        # Add the number to the result list
        result_numbers.append(num)

# Display the result
print("Numbers divisible by 7 but not by 5 in the range 2000 to 3500:")
print(result_numbers)

"""The below python program helps you to find all the palindrome numbers from the starting and ending numbers, these numbers are supplied as input to the program.

Palindrome Number - A palindrome number is a number that reads the same forward and backward. In other words, if you reverse the digits of a palindrome number, you get the same number. For example, 121 is a palindrome number because if you read it backward, it is still 121.
"""

def is_palindrome(number):
    """Check if a number is a palindrome."""
    return str(number) == str(number)[::-1]

def count_palindromes(start, end):
    """Count palindromic numbers in the given range."""
    count = 0
    for num in range(start, end + 1):
        if is_palindrome(num):
            count += 1
    return count

# Define the range
start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))

# Check and display the result
if start_range > end_range:
    print("Invalid input: Starting number should be less than or equal to the ending number.")
else:
    palindrome_count = count_palindromes(start_range, end_range)
    print(f"Number of palindromic numbers in the range {start_range} to {end_range}: {palindrome_count}")

"""This Python program takes a number as input andr returns true if the sum of its digits has the same parity as the entire number. (Here same parity is whether they are even or odd). Else would return false."""

# "Create a function that takes a number as input and returns True if the sum of its digits has the same parity as the entire number. Otherwise, return False.
# parity_analysis(243) ➞ True  # 243 is odd and so is 9 (2 + 4 + 3)
# parity_analysis(12) ➞ False  # 12 is even but 3 is odd (1 + 2)"

number = int(input("Enter number: "))
number_str = str(abs(number))
digit_sum = 0

for digit in number_str:
  digit_sum += int(digit)

    # Check if the sum has the same parity as the entire number
print(number % 2 == digit_sum % 2)

"""The below python program helps you to calculate factorial of a given number.

Factorial - Calculating the factorial of a number involves multiplying all positive integers up to that number.
Here's a simple Python program to calculate the factorial of a given number.
"""

# Factorial of the given number.
number = int(input("Enter a number: "))
result = 1
for i in range(2, number + 1):
    result *= i

print(f"The factorial of {number} is {result}")