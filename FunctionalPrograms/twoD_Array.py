try:
    row=int(input("Enter rows size: "))
    column=int(input("Enter column size: "))
    element=[]

    print("Enter the entries:")
    for i in range(row):
        a = []
        for j in range(column):
            a.append(int(input()))
        element.append(a)

    print(element)
except Exception:
    print("Exception Error ")
