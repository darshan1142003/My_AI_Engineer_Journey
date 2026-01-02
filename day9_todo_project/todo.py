tasks = []

try:
    with open("file.txt", "r") as f:
        tasks=f.read().splitlines()

except:
    pass

while True:
    print("\n1. Add Task")
    print("\n2. View Task")
    print("\n3. Delete Task")
    print("\n4. Exit")

    choice=input("enter choice: ")

    if choice == '1':
        task = input("enter task: ")
        tasks.append(task)

        with open("file.txt", "w") as f:
            for t in tasks:
                f.write(t + "\n")

        print("task added")

    elif choice == "2":
        if len(tasks)==0:
            print("no tasks")

        else:
            for i in range(len(tasks)):
                print(i+1,tasks[i])

    elif choice == "3":
        for i in range(len(tasks)):
                print(i+1,tasks[i])
        num = int(input("enter task number: "))

        if 1 <= num <= len(tasks):
            tasks.pop(num-1)

            with open("file.txt", "w") as f:
                for t in tasks:
                    f.write(t + "\n")
            print("task deleted")

        else:
            print("invalid number")    

    elif choice == "4":
            print("bye") 
            break
    
    else:
        print("wrong choice")       