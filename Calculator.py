
import math
import sys
import os
from xml.dom.pulldom import IGNORABLE_WHITESPACE
print("Welcome to the calculator!")
print("These are the available operations:")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")
print("5. Exponentiation(^)")
print("6. Square Root(sqrt)")
print("7. Logarithm(log)")
print("8. Sinus(sin) [radians]")
print("9. Cosinus(cos) [radians]")
print("10. Tangens(tan) [radians]")
print("^-1 is the inverse of the function or number")
print("^2 is the square of the number")
print("^3 is the cube of the number")
print("^4 is the fourth power of the number")
number1 = input("Type out your first number: ")
try:
    number1 = float(number1)
except ValueError:
    print("You have to type a number!")
    sys.exit()
operator1 = input("Type out your operator: ")
try:
   if operator1 == '+' or '-' or '*' or '/' or '^' or 'sqrt' or 'log' or 'sin' or 'cos' or 'tan' or IGNORABLE_WHITESPACE('sin^-1') or IGNORABLE_WHITESPACE('cos^-1') or IGNORABLE_WHITESPACE('tan^-1'):
         pass
except ValueError:
    print("You have to type a valid operator!")
    sys.exit()
number2 = input("Type out your second number: ")

try:
    number2 = float(number2)
except ValueError:
    print("You have to type a number!")
    sys.exit()
if operator1 == '+':
    print(number1 + number2)
elif operator1 == '-':
    print(number1 - number2)
elif operator1 == '*':
    print(number1 * number2)
elif operator1 == '/':
    print(number1 / number2)
elif operator1 == '^':
    print(number1 ** number2)
elif operator1 == 'sqrt':
    print(math.sqrt(number1))
elif operator1 == 'log':
    print(math.log(number1))
elif operator1 == 'sin':
    print(math.sin(number1))
elif operator1 == 'cos':
    print(math.cos(number1))
elif operator1 == 'tan':
    print(math.tan(number1))
elif operator1 == 'sin^-1':
    print(math.asin(number1))
elif operator1 == 'cos^-1':
    print(math.acos(number1))
elif operator1 == 'tan^-1':
    print(math.atan(number1))
    