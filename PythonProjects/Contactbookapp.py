contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print(" No contacts found.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name} | Phone: {details['phone']}")

def search_contact():
    search = input("Enter name or phone to search: ")
    found = False

    for name, details in contacts.items():
        if search.lower() == name.lower() or search == details["phone"]:
            print("\n Contact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
            break

    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")

    if name in contacts:
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print("🗑 Contact deleted successfully!")
    else:
        print("Contact not found.")

# User Interface
while True:
    print("\n====== Contact Book Menu ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print(" Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
