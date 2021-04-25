import math

def distance(x1, y1):
    diff = math.sqrt((x1 ** 2 + y1 ** 2))
    print(diff)

try:
    x = int(input("Enter number 1 : "))
    y = int(input("Enter number 2 : "))
    if x <= 0 or x >= 1000 or y <= 0 or y >= 1000:

        distance(x, y)
except Exception:
    print("Exception occured")