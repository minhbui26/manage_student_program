import csv

FILENAME = 'student.csv'

def load_students():
    students = []
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['student_code'] = int(row['student_code'])
            row['total_score'] = float(row['total_score'])
            students.append(row)
    return students

def save_students(students):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['student_code', 'student_name', 'total_score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

def input_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a float number.")

def add_student(students):
    student_code = input_integer("Enter student code: ")
    student_name = input("Enter student name: ")
    total_score = input_float("Enter total score: ")
    students.append({'student_code': student_code, 'student_name': student_name, 'total_score': total_score})
    save_students(students)  # Save immediately after adding

def edit_student(students):
    student_code = input_integer("Enter student code to edit: ")
    for student in students:
        if student['student_code'] == student_code:
            student['student_name'] = input(f"Enter new name for {student['student_name']} (or press Enter to keep current): ") or student['student_name']
            new_score = input(f"Enter new score for {student['total_score']} (or press Enter to keep current): ")
            student['total_score'] = float(new_score) if new_score else student['total_score']
            save_students(students)  # Save immediately after editing
            return
    print("Student not found.")

def delete_student(students):
    student_code = input_integer("Enter student code to delete: ")
    for student in students:
        if student['student_code'] == student_code:
            students.remove(student)
            save_students(students)  # Save immediately after deleting
            return
    print("Student not found.")

def search_students(students):
    criterion = input("Search by (code/name/score): ").strip().lower()
    query = input("Enter search value: ").strip()
    if criterion == 'code':
        query = int(query)
    elif criterion == 'score':
        query = float(query)

    results = [student for student in students if str(student[criterion]) == str(query)]
    for student in results:
        print(f"Code: {student['student_code']}, Name: {student['student_name']}, Score: {student['total_score']}")

def print_students(students):
    for student in students:
        print(f"Code: {student['student_code']}, Name: {student['student_name']}, Score: {student['total_score']}")

def main():
    students = load_students()
    while True:
        print("\nClassroom Management System")
        print("1. Add student")
        print("2. Edit student")
        print("3. Delete student")
        print("4. Search student")
        print("5. Print all students")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            edit_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            search_students(students)
        elif choice == '5':
            print_students(students)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
