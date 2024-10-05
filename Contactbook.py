# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter home address: ")
    
    # Save the contact details in the contacts dictionary
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact {name} added successfully!\n")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")
    else:
        print("No contacts saved yet!\n")

# Function to search for a contact by name or phone number
def search_contact():
    search = input("Enter contact name or phone number to search: ")
    
    for name, details in contacts.items():
        if search == name or search == details['Phone']:
            print(f"Found Contact - Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}\n")
            return
    print("Contact not found!\n")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    
    if name in contacts:
        print(f"Updating contact details for {name}")
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new home address: ")
        
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"Contact {name} updated successfully!\n")
    else:
        print("Contact not found!\n")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!\n")
    else:
        print("Contact not found!\n")

# Main program loop
def contact_manager():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
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
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option! Please choose a number between 1 and 6.\n")

# Run the contact manager program
contact_manager()
