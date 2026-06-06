students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student Added Successfully!\n")


def view_students():
    if len(students) == 0:
        print("No Students Found!\n")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"Roll No: {student['roll']}")
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print("-" * 20)


def search_student():
    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print(f"Roll No: {student['roll']}")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            return

    print("Student Not Found!\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!\n")
            return

    print("Student Not Found!\n")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Try Again.\n")