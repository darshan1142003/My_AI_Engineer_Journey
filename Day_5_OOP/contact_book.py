class ContactBook:
    def __init__(self, filename="contacts.txt"):
        self.filename=filename

    def addcontacts(self, name, phone):
        with open(self.filename, "a") as f:
            f.write(f"{name}, {phone}\n")
        print("contact added successfully")

    def ViewContacts(self):
        with open(self.filename,"r") as f:
            print("\n--contact list--")
            for line in f:
                print(line)

book=ContactBook()

while True:
    print("\n1.Add Contact")
    print("2.View Contact")
    print("3.Exit")

    choice= input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter Phone: ")
        book.addcontacts(name, phone)

    elif choice == "2":
        book.ViewContacts()

    elif choice == "3":
        print("Thankyou!!")
        break

    else:
        print("Invalid Choice")
        