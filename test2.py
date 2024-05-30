import csv

# Define the CSV file path
CSV_FILE = 'students.csv'

# Load students from the CSV file
def load_students():
    students = {}
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_code = int(row['student_code'])
                students[student_code] = {
                    'student_name': row['student_name'],
                    'total_score': float(row['total_score'])
                }
    except FileNotFoundError:
        print(f"{CSV_FILE} not found, starting with an empty student list.")
    return students

# Save students to the CSV file
def save_students(students):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ['student_code', 'student_name', 'total_score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for code, data in students.items():
            writer.writerow({'student_code': code, 'student_name': data['student_name'], 'total_score': data['total_score']})

# Add a new student
def add_student(students):
    try:
        student_code = input("Enter student code (8 digits): ")
        if not student_code.isdigit() or len(student_code) != 8:
            print("Invalid student code. Please enter 8 digits.")
            return
        student_code = int(student_code)
        if student_code in students:
            print("Student code already exists.")
            return
        student_name = input("Enter student name: ")
        total_score = float(input("Enter total score: "))
        if total_score > 4:
            print("Total score cannot be greater than 4.")
            return
        students[student_code] = {'student_name': student_name, 'total_score': total_score}
        save_students(students)
    except ValueError as e:
        print(f"Invalid input: {e}")

# Edit an existing student
def edit_student(students):
    try:
        student_code = input("Enter student code to edit (8 digits): ")
        if not student_code.isdigit() or len(student_code) != 8:
            print("Invalid student code. Please enter 8 digits.")
            return
        student_code = int(student_code)
        if student_code not in students:
            print("Student code not found.")
            return
        student_name = input("Enter new student name: ")
        total_score = float(input("Enter new total score: "))
        if total_score > 4:
            print("Total score cannot be greater than 4.")
            return
        students[student_code] = {'student_name': student_name, 'total_score': total_score}
        save_students(students)
    except ValueError as e:
        print(f"Invalid input: {e}")

# Delete a student
def delete_student(students):
    try:
        student_code = input("Enter student code to delete (8 digits): ")
        if not student_code.isdigit() or len(student_code) != 8:
            print("Invalid student code. Please enter 8 digits.")
            return
        student_code = int(student_code)
        if student_code in students:
            del students[student_code]
            save_students(students)
            print(f"Student with code {student_code} has been deleted.")
        else:
            print("Student code not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")

# Search student by code
def search_student_by_code(students):
    try:
        student_code = input("Enter student code to search (8 digits): ")
        if not student_code.isdigit() or len(student_code) != 8:
            print("Invalid student code. Please enter 8 digits.")
            return
        student_code = int(student_code)
        if student_code in students:
            print(students[student_code])
        else:
            print("Student not found.")
    except ValueError as e:
        print(f"Invalid input: {e}")

# Main menu
def main():
    students = load_students()
    while True:
        print("\nClassroom Management Program")
        print("1. Add student")
        print("2. Edit student")
        print("3. Delete student")
        print("4. Search student by code")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            edit_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            search_student_by_code(students)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
