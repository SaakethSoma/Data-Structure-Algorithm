from storage import load_books, save_books

def add_book(title):
    books = load_books()
    books.append(title)
    save_books(books)
    print("book added")

def view_books():
    books = load_books()
    for b in books:
        print(b)
        
def remove_book(title):
    books = load_books()
    if title in books:
        books.remove(title)
        save_books(books)
        print("book removed")
    else:
        print("book not found")