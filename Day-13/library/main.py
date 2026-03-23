from library import add_book, view_books, remove_book
while True: 
    print("1. Add book")
    print("2. View books")
    print("3. Remove book")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter book title: ")
        add_book(title)
    elif choice == "2":
        view_books()
    elif choice == "3":
        title = input("Enter book title: ")
        remove_book(title)
    elif choice == "4":
        break
    else:
        print("Invalid choice")