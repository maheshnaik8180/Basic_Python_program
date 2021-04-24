import random
try:
    numberOfFlips = int(input("how many times flip the coin"))

    def flipcoin(NumberOfFlips):
        head = 0
        tail = 0
        for i in range(NumberOfFlips):
            num = random.random()
        if num < 0.5:
            head += 1
        else:
            tail += 1
        headPercent = (head / numberOfFlips) * 100
        tailPercent = (head / numberOfFlips) * 100
        return headPercent, tailPercent


    headpercent, tailpercent = flipcoin(numberOfFlips)
    print(F"Head percent is {headpercent}% ")
    print(F"Tail percent is {tailpercent}% ")
except Exception:
    print("Exception occured")
