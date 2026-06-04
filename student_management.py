import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

conn.commit()


# Add Student
def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    cursor.execute("""
    INSERT INTO students (name, age, course)
    VALUES (?, ?, ?)
    """, (name, age, course))

    conn.commit()
    print("Student Added Successfully!")


# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n===== STUDENT RECORDS =====")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print(f"\nID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
        print("------------------------")


# Update Student
def update_student():
    student_id = input("Enter Student ID to Update: ")

    new_name = input("Enter New Name: ")
    new_age = input("Enter New Age: ")
    new_course = input("Enter New Course: ")

    cursor.execute("""
    UPDATE students
    SET name = ?, age = ?, course = ?
    WHERE id = ?
    """, (new_name, new_age, new_course, student_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Updated Successfully!")
    else:
        print("Student ID not found.")


# Delete Student
def delete_student():
    student_id = input("Enter Student ID to Delete: ")

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student ID not found.")


# Main Menu Loop
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program Closed Successfully!")
        break

    else:
        print("Invalid Choice! Please try again.")


# Close connection
conn.close()