a = int(input("enter num1: "))
b = int(input("enter num2: "))
c = int(input("enter num3: "))

def max():
    if ((a > b) and (a > c)):
        print(f"{a} is maximum")
    elif ((b > a) and (b > c)):
        print(f"{b} is maximum")
    elif ((c > a) and (c > b)):
        print(f"{c} is maximum")

max()        