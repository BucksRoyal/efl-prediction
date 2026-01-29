# Contact Book with Custom KeyError

contacts = {}  # stores contacts as {name: phone}


def add_contact(name, phone):
    if name in contacts:
        raise KeyError(f"Contact '{name}' already exists!")  # custom KeyError
    contacts[name] = phone


# Main loop
while True:
    print("\nContact Book Options:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        try:
            add_contact(name, phone)
            print(f"Contact '{name}' added successfully!")
        except KeyError as e:
            print(e)  # friendly message if contact exists

    elif choice == "2":
        if contacts:
            print("Contacts List:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts available.")

    elif choice == "3":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")
