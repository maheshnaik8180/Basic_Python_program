
import math
def quad(num1,num2,num3):
    delta = num2 * num2 - 4 * num1 * num3
    """print absolute value"""
    print(abs(delta))
    """using square root function """
    root1 = (-num2 + math.sqrt(abs(delta))) / (2 * num1)
    root2 = (-num2 - math.sqrt(abs(delta))) / (2 * num1)
    print("root 1: ", root1)
    print("root 2 : ", root2)

try:
    """give the user input for three numbers"""
    number1 = int(input("Enter number 1 :"))
    number2 = int(input("Enter number 2 :"))
    number3 = int(input("Enter number 3 :"))
    if number1 <= 0 or number1 >= 1000 or number2 <= 0 or number2 >= 1000 and number3 <= 0 or number3 >= 1000:
        print("Enter number between o and 1000.")
    quad(number1, number2, number3)
except Exception:
    print("Please enter numbers in valid range.")