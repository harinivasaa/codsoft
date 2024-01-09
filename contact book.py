contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print(f"Added {name} with number {number} to contacts.")

def find_contact(name):
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}.")
    else:
        print(f"{name} is not in the contacts.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} is not in the contacts.")

def display_contacts():
    print("Contacts:")
    for name, number in contacts.items():
        print(f"{name}: {number}")

# Menu for user interaction
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Find Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == '2':
        name = input("Enter name to find: ")
        find_contact(name)
    elif choice == '3':
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        print("Exiting contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
