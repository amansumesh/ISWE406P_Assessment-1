def welcome():
    print("\nWelcome to LMS Portal")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

library = []
students = []

admin_uname = "admin"
admin_password = "admin123"

def register_student(name, student_id, password):
    students.append({
        "name": name,
        "id": student_id,
        "password": password
    })
    print("Student registered successfully\n")

def student_login(student_id, password):
    for s in students:
        if s["id"] == student_id and s["password"] == password:
            print(f"Welcome {s['name']} (Student)\n")
            return True
    print("Invalid student credentials\n")
    return False

def admin_login(username, password):
    return username == admin_uname and password == admin_password

def add_book(title, author):
    library.append({"title": title, "author": author})
    print("Book added successfully\n")

def delete_book(title):
    for book in library:
        if book["title"] == title:
            library.remove(book)
            print("Book deleted successfully\n")
            return
    print("Book not found\n")

def view_books():
    if not library:
        print("No books available\n")
    else:
        for book in library:
            print(f"- {book['title']} ({book['author']})")
        print()

while True:
    welcome()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        sid = input("Enter student ID: ")
        pwd = input("Create password: ")
        register_student(name, sid, pwd)

    elif choice == "2":
        role = input("Login as (admin/student): ").lower()

        if role == "admin":
            u = input("Username: ")
            p = input("Password: ")

            if admin_login(u, p):
                print("Admin login successful\n")
                add_book("Python Basics", "Preeti Arora")
                delete_book("Python Basics")
            else:
                print("Invalid admin credentials\n")

        elif role == "student":
            sid = input("Student ID: ")
            pwd = input("Password: ")

            if student_login(sid, pwd):
                view_books()

        else:
            print("Invalid role\n")

    elif choice == "3":
        print("Exiting system...")
        break

    else:
        print("Invalid choice\n")
