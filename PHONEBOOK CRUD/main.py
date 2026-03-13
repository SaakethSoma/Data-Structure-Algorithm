from operations import add_contact,search_contact,update_contact, delete_contact,display_contact
while True:
    print("\n ---Phonebook Menu---") 
    print("1. Add Contact")
    print("2. Search Contacts")
    print("3. Update Contact")
    print("4. Delete Contacts")
    print("5. Display Contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        display_contact()
    elif choice == '6':
        print("Exiting Phonebook.")
        break
    else:
        print("Invalid choice. Please try again.")