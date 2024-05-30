import csv
import tkinter as tk
from tkinter import messagebox, simpledialog

FILENAME = 'Danh_sach.csv'

# Load students from the CSV file
def load_students():
    students = []
    try:
        with open(FILENAME, encoding='utf-8', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['student_code'] = int(row['student_code'])
                row['total_score'] = float(row['total_score'])
                students.append(row)
    except FileNotFoundError:
        with open(FILENAME, encoding='utf-8', mode='w', newline='') as file:
            fieldnames = ['student_code', 'student_name', 'total_score']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
    return students

# Save students to the CSV file
def save_students(students):
    with open(FILENAME, encoding='utf-8', mode='w', newline='') as file:
        fieldnames = ['student_code', 'student_name', 'total_score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

# Input an integer with validation
def input_integer(prompt):
    while True:
        try:
            value = int(simpledialog.askstring("Input", prompt))
            return value
        except (ValueError, TypeError):
            messagebox.showerror("Invalid input", "Please enter an integer.")

# Input a float with validation
def input_float(prompt):
    while True:
        try:
            value = float(simpledialog.askstring("Input", prompt))
            return value
        except (ValueError, TypeError):
            messagebox.showerror("Invalid input", "Please enter a float number.")

# Add a new student
def add_student(students):
    student_code = input_integer("Enter student code: ")
    student_name = simpledialog.askstring("Input", "Enter student name: ")
    total_score = input_float("Enter total score: ")
    students.append({'student_code': student_code, 'student_name': student_name, 'total_score': total_score})
    save_students(students)
    messagebox.showinfo("Info", "Student added successfully.")

# Edit an existing student
def edit_student(students):
    student_code = input_integer("Enter student code to edit: ")
    for student in students:
        if student['student_code'] == student_code:
            student['student_name'] = simpledialog.askstring("Input", f"Enter new name for {student['student_name']} (or press Enter to keep current): ") or student['student_name']
            new_score = simpledialog.askstring("Input", f"Enter new score for {student['total_score']} (or press Enter to keep current): ")
            student['total_score'] = float(new_score) if new_score else student['total_score']
            save_students(students)
            messagebox.showinfo("Info", "Student edited successfully.")
            return
    messagebox.showerror("Error", "Student not found.")

# Delete a student
def delete_student(students):
    student_code = input_integer("Enter student code to delete: ")
    for student in students:
        if student['student_code'] == student_code:
            students.remove(student)
            save_students(students)
            messagebox.showinfo("Info", "Student deleted successfully.")
            return
    messagebox.showerror("Error", "Student not found.")

# Search for students
def search_students(students):
    student_code = input_integer("Enter student code to search: ")
    results = [student for student in students if student['student_code'] == student_code]
    if results:
        student = results[0]
        result_text = f"Code: {student['student_code']}, Name: {student['student_name']}, Score: {student['total_score']}"
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", "No matching students found.")

# Print all students
def print_students(students):
    result_text = "\n".join(f"Code: {student['student_code']}, Name: {student['student_name']}, Score: {student['total_score']}" for student in students)
    messagebox.showinfo("All Students", result_text)

# Main function to run the application
def main():
    students = load_students()

    root = tk.Tk()
    root.title("Classroom Management System")

    def on_add():
        add_student(students)

    def on_edit():
        edit_student(students)

    def on_delete():
        delete_student(students)

    def on_search():
        search_students(students)

    def on_print():
        print_students(students)

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="Add Student", command=on_add).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(frame, text="Edit Student", command=on_edit).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame, text="Delete Student", command=on_delete).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame, text="Search Student", command=on_search).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(frame, text="Print All Students", command=on_print).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    tk.Button(frame, text="Exit", command=root.quit).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
