n = int(input("enter number: "))
def facto():
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(f"factorial is {fact}")    
facto()    