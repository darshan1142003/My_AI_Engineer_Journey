a = int(input("enter number you want check: "))

def check():
    if(a % 2 == 0):
        print(f"{a} is the even number.")
    else:
        print(f"{a} is the odd number.")

check()