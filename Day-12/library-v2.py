#Library v2(persistent storage)
#upgrade from library v1
#new features:
# - Data saved in a file
# - program remembers book after restart

import json
#load library data
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except:
        return {}
    
#save library data
def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file)

#add book 
def add_book(library):
    book=input("Enter book name: ")
    author=input("Enter author name: ")
    library[book]=author
    save_library(library)
    print("Book added successfully!")
#view book
def view_book(library):
    if len(library) == 0:
        print("No books in library.")
    else:
        for book in library:
            print(book, "by", library[book])

#delete book
def delete_book(library):
    book=input("Enter book name to delete: ")
    if book in library:
        del library[book]
        save_library(library)
        print("Book deleted successfully!")
    else:
        print("Book not found in library.")

#main program
def main():
    library=load_library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Exit")
        choice=input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_book(library)
        elif choice == "3":
            delete_book(library)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
main()