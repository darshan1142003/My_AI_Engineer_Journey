def check(a):
    if (a <= 1):
        print(f"{a} is not prime number.")
        return
    
    for i in range(2, a):
        if(a % i == 0):
            print(f"{a} is not prime number.")
            return

    print(f"{a} is the prime number.")

num = int(input("enter number you want check: "))
check(num)