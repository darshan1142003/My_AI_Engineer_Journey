num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))
num3 = int(input("enter the number 3: "))

if((num1>num2) and (num1>num3)):
    print("number 1 is largest")
elif((num2>num1) and (num2>num3)):
    print("number 2 is largest")
elif((num3>num1) and (num3>num2)):
    print("number 3 is largest")    
