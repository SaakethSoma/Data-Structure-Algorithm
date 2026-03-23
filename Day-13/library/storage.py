import json

FILE="data.json"
def load_books():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except :
        return []
def save_books(books):
    with open(FILE, "w") as f:
        json.dump(books, f)
        