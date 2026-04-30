import random
import string
import json

# Load data
try:
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
except:
    passwords = {}

# Generate password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return "".join(random.choice(chars) for _ in range(12))

# Save data
def save_data():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)

while True:
    print("\n----------PASSWORD MANAGER-----------")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Delete Password")
    print("5. Update Password")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    # 1. Save Password
    if choice == "1":
        website = input("Enter Website Name: ")
        password = input("Enter Password (leave blank to generate): ")

        if password == "":
            password = generate_password()

        if website in passwords:
            print("Website already exists. Updating password...")

        passwords[website] = password
        save_data()

        print("Password saved successfully ")

    # 2. View Passwords
    elif choice == "2":
        if not passwords:
            print("No Passwords Found")
        else:
            for site, pwd in passwords.items():
                print(f"{site}: {pwd}")

    # 3. Generate Password
    elif choice == "3":
        print("Generated Password:", generate_password())

    # 4. Delete Password
    elif choice == "4":
        website = input("Enter Website Name to Remove: ")

        if website in passwords:
            del passwords[website]
            save_data()
            print(f"{website} removed successfully ")
        else:
            print("Website not found ")

    # 5. Update Password
    elif choice == "5":
        website = input("Enter Website Name to Update: ")

        if website in passwords:
            new_password = input("Enter New Password (leave blank to generate): ")

            if new_password == "":
                new_password = generate_password()

            passwords[website] = new_password
            save_data()
            print(f"{website} updated successfully ")
        else:
            print("Website not found ")

    # 6. Exit
    elif choice == "6":
        print("Exit")
        break

    # Invalid input
    else:
        print("Invalid Choice")