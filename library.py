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

students = []

def register_student(student_name, student_id):
    student = {
        "name": student_name,
        "id": student_id
    }
    students.append(student)
    print(f"Student '{student_name}' (ID: {student_id}) registered successfully")

def view_students():
    if not students:
        print("No students registered")
    else:
        print("Registered Students:")
        for s in students:
            print(f"- {s['id']} : {s['name']}")

welcome()
add_book("Python Basics", "Preeti Arora")
add_book("Java Fundamentals", "Herbert Schildt")
view_books()

delete_book("Python Basics")
view_books()

print("\n--- Student Registration Module ---")
register_student("Aman Sumesh", "23CSE101")
register_student("Ravi Kumar", "23CSE102")
view_students()
