#Library Project
library = {}
def add_book():
    book=input("Enter the book name: ")
    author=input("Enter the author name: ")

    library[book]=author
    print("Book added successfully!")
def view_books():
    if len(library)==0:
        print("No books in the library.")
    else:
        for book in library:
            print(book,"by",library[book])
def search_book():
    book=input("Enter the book name to search: ")
    if book in library:
        print("Author:",library[book])
    else:
        print("Book not found in the library.")
def delete_book():
    book=input("Enter the book name to delete: ")
    if book in library:
        del library[book]
        print("Book deleted successfully!")
    else:
        print("Book not found in the library.")
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            add_book()
        elif choice=="2":
            view_books()
        elif choice=="3":
            search_book()
        elif choice=="4":
            delete_book()
        elif choice=="5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()