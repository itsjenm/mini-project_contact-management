import re

contacts = {
    'john.doe@example.com': {
        'name': 'John Doe',
        'phone': '123-456-7890',
        'email': 'john.doe@example.com',
        'address': '123 Elm Street',
        'notes': 'Friend from school'
    },
    'jane.doe@example.com': {
        'name': 'Jane Doe',
        'phone': '421-345-9000',
        'email': 'jane.doe@example.com',
        'address': '302 Miracle Street',
        'notes': 'Colleague'
    },
    'michael.burry@example.com': {
        'name': 'Michael Burry',
        'phone': '333-897-7899',
        'email': 'michael.burry@example.com',
        'address': '900 Wall Street',
        'notes': 'Hedge fund investor'
    }
}


def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")


def add_contact():
    email = input("Enter email address: ")
    if email in contacts:
        print("Contact already exists!")
        return
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    notes = input("Enter notes: ")
    contacts[email] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address,
        'notes': notes
    }
    print("Contact added successfully!")


def edit_contact():
    email = input("Enter email address of the contact to edit: ")
    if email not in contacts:
        print("Contact not found!")
        return
    name = input("Enter new name: ")
    phone = input("Enter new phone number: ")
    address = input("Enter new address: ")
    notes = input("Enter new notes: ")
    contacts[email] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address,
        'notes': notes
    }
    print("Contact updated successfully!")


def delete_contact():
    email = input("Enter email address of the contact to delete: ")
    if email in contacts:
        del contacts[email]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


def search_contact():
    email = input("Enter email address to search: ")
    if email in contacts:
        print(contacts[email])
    else:
        print("Contact not found!")


def display_all_contacts():
    for email, details in contacts.items():
        print(f"Email: {email}, Name: {details['name']}, Phone: {details['phone']}")


def export_contacts(filename):
    with open(filename, 'w') as file:
        for email, details in contacts.items():
            file.write(f"{email},{details['name']},{details['phone']},{details['address']},{details['notes']}\n")
    print("Contacts exported successfully!")


def import_contacts(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone, email, address, notes = line.strip().split(',')
                contacts[email] = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'address': address,
                    'notes': notes
                }
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("File not found!")



def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def is_valid_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            filename = input("Enter filename to export contacts: ")
            export_contacts(filename)
        elif choice == '7':
            filename = input("Enter filename to import contacts: ")
            import_contacts(filename)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


main()