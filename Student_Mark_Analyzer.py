import sqlite3
import pandas as pd

# ==============================
# DATABASE SETUP
# ==============================
conn = sqlite3.connect("student_system.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    math INTEGER,
    science INTEGER,
    english INTEGER
)
""")

conn.commit()

# Insert default admin (only first time)
cursor.execute("SELECT * FROM admin")
if not cursor.fetchall():
    cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)",
                   ("admin", "admin123"))
    conn.commit()


# ==============================
# LOGIN SYSTEM
# ==============================
def login():
    print("\n===== LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")

    cursor.execute("SELECT * FROM admin WHERE username=? AND password=?",
                   (username, password))

    if cursor.fetchone():
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Credentials!\n")
        return False


# ==============================
# ADD STUDENT
# ==============================
def add_student():
    print("\n===== ADD STUDENT =====")
    name = input("Name: ")
    math = int(input("Math Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))

    cursor.execute("""
    INSERT INTO students (name, math, science, english)
    VALUES (?, ?, ?, ?)
    """, (name, math, science, english))

    conn.commit()
    print("Student Added Successfully!\n")


# ==============================
# VIEW STUDENTS
# ==============================
def view_students():
    print("\n===== ALL STUDENTS =====")
    df = pd.read_sql_query("SELECT * FROM students", conn)

    if df.empty:
        print("No students found!\n")
        return

    df["total"] = df["math"] + df["science"] + df["english"]
    df["average"] = df["total"] / 3

    def grade(avg):
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        else:
            return "C"

    df["grade"] = df["average"].apply(grade)

    print(df)


# ==============================
# SEARCH STUDENT
# ==============================
def search_student():
    print("\n===== SEARCH STUDENT =====")
    name = input("Enter name to search: ")

    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    data = cursor.fetchall()

    if not data:
        print("Student not found!\n")
        return

    for row in data:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Math:", row[2])
        print("Science:", row[3])
        print("English:", row[4])
        print("--------------------")


# ==============================
# MAIN MENU
# ==============================
def menu():
    while True:
        print("\n===== STUDENT MARK SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting System...")
            break
        else:
            print("Invalid Choice!")


# ==============================
# RUN PROGRAM
# ==============================
if login():
    menu()
