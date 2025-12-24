class Calculator:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2

    def Add(self):
        print(f"Addition of {self.num1} and {self.num2} is {self.num1 + self.num2}")
    def Sub(self):
        print(f"Subtraction of {self.num1} and {self.num2} is {self.num1 - self.num2}")
    def Mul(self):
        print(f"Multiplication of {self.num1} and {self.num2} is {self.num1 * self.num2}")
    def Div(self):
        print(f"Division of {self.num1} and {self.num2} is {self.num1 / self.num2}")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c=Calculator(a,b)
c.Add()        