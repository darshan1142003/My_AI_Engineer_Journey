FILE_NAME = "contact.txt"

def load_contacts():
    contacts = {}
    try:
        with open(FILE_NAME,"r") as f:
            for line in f:
                name, phone = line.strip().split(",")
            contacts[name]=phone
    except:
        with open(FILE_NAME, "w") as f:
            pass

    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        for name in contacts:
            f.write(name + "," + contacts[name] + "\n")

def add_contacts(contacts):
    name=input("enter name: ").strip()
    phone=input("enter phone: ").strip()

    if name == "" or phone=="":
        print("invalid input")
        return
    
    contacts[name]=phone
    save_contacts(contacts)
    print("contact added")

def view_contacts(contacts):
    if not contacts:
        print("no contacts")
        return
    for name, phone in contacts.items():
        print(name, ":", phone)

def search_contacts(contacts):
    name = input("enter name to search: ").strip()
    if name in contacts:
        print(name, ":", contacts[name])
    else:
        print("not found")

def delete_contacts(contacts):
    name = input("enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("contact deleted") 
    else:
        print("not found")

def main():
    contacts=load_contacts()

    while True:
        print("\n1.Add contact")
        print("\n2.View contacts")
        print("\n3.Search contacts")
        print("\n4.Delete contacts")
        print("\n5.Exit")

        choice = input("enter choice: ")

        if choice=="1":
            add_contacts(contacts)    
        elif choice=="2":
            view_contacts(contacts)    
        elif choice=="3":
            search_contacts(contacts)    
        elif choice=="4":
            delete_contacts(contacts)    
        elif choice=="5":
            save_contacts(contacts)
            print("bye")
            break    
        else:
            print("invalid")

main()            