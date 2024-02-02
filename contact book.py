class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def display_contact(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = Contact(name, phone, email, address)

    def view_contact_list(self):
        for name, contact in self.contacts.items():
            print(f"{name}: {contact.phone}")

    def search_contact(self, query):
        found = []
        for name, contact in self.contacts.items():
            if query.lower() in name.lower() or query.lower() in contact.phone.lower():
                found.append((name, contact))
        if found:
            for name, contact in found:
                print(f"{name}: {contact.phone}")
        else:
            print("No contacts found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            contact = self.contacts[name]
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            if address:
                contact.address = address
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found.")


contact_book = ContactBook()

while True:
    print("\n1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact_book.add_contact(name, phone, email, address)
    elif choice == '2':
        contact_book.view_contact_list()
    elif choice == '3':
        query = input("Enter search query: ")
        contact_book.search_contact(query)
    elif choice == '4':
        name = input("Enter name: ")
        phone = input("Enter new phone number (press enter to keep the same): ")
        email = input("Enter new email (press enter to keep the same): ")
        address = input("Enter new address (press enter to keep the same): ")
        contact_book.update_contact(name, phone, email, address)
    elif choice == '5':
        name = input("Enter name: ")
        contact_book.delete_contact(name)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")