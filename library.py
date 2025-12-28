def welcome():
    print("Welcome to Library Management System\n")

library = []

def add_book(book_name, author_name):
    book = {
        "title": book_name,
        "author": author_name
    }
    library.append(book)
    print(f"Book '{book_name}' by {author_name} added successfully")

def view_books():
    if not library:
        print("\nNo books available")
    else:
        print("\nAvailable books:")
        for book in library:
            print(f"- {book['title']} (Author: {book['author']})")
    print("\n")

def delete_book(book_name):
    for book in library:
        if book["title"] == book_name:
            library.remove(book)
            print(f"Book '{book_name}' deleted successfully")
            return
    print(f"Book '{book_name}' not found")

welcome()
add_book("Python Basics", "Preeti Arora")
add_book("Java Fundamentals", "Herbert Schildt")
view_books()

delete_book("Python Basics")
view_books()
