# Contact Book Application

contacts={}

def add_contact():
    name=input("Enter name: ")
    phone=input("Enter phone number: ")
    email=input("Enter email: ")
    address=input("Enter address: ")
    contacts[name]={"phone": phone, "email": email, "address": address}
    print(f"✅ Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n📒 Contact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")
    print()

def search_contact():
    search=input("Enter name or phone number to search: ")
    found=False
    for name, info in contacts.items():
        if search.lower()==name.lower() or search==info["phone"]:
            print("\n🔍 Contact Found:")
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}\n")
            found=True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name=input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Leave blank if you don't want to change a field.")
        phone=input("Enter new phone number: ")
        email=input("Enter new email: ")
        address=input("Enter new address: ")

        if phone:
            contacts[name]["phone"]=phone
        if email:
            contacts[name]["email"]=email
        if address:
            contacts[name]["address"]=address

        print(f"✅ Contact '{name}' updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name=input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted successfully!\n")
    else:
        print("Contact not found.\n")

def menu():
    while True:
        print("📌 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice=input("Choose an option (1-6): ")

        if choice=="1":
            add_contact()
        elif choice=="2":
            view_contacts()
        elif choice=="3":
            search_contact()
        elif choice=="4":
            update_contact()
        elif choice=="5":
            delete_contact()
        elif choice=="6":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
