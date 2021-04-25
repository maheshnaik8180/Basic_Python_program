"""given user input find harmonic function """

try:

    number = int(input("Enter the value of nth number : "))
    s = 0.0
    for num in range(1, number + 1):
        s = s + 1 / num
    print("Sum is: ", round(s, 3))

except Exception:
    print("Exception occurred")