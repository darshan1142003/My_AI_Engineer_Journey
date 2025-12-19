num1= int(input("enter first value :"))
num2= int(input("enter second value :"))

operator = input("enter the operator you want to perform : (+,-,*,/)")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("invalid operator") 
