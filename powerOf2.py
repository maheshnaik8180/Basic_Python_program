try:
    power = int(input("enter number :"))


    def powerOfTwo(power):

        for i in range(power + 1):
            print(f"2^{i}={2 ** i}")

        print("print valid data type")


    powerOfTwo(power)
except Exception:
    print("exception occured")
