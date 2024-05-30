#test giao diện
import csv
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

FILENAME = 'student.csv'

def load_students():
    students = []
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['student_code'] = int(row['student_code'])
                row['total_score'] = float(row['total_score'])
                students.append(row)
    except FileNotFoundError:
        with open(FILENAME, mode='w', newline='') as file:
            fieldnames = ['student_code', 'student_name', 'total_score']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
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
            value = int(simpledialog.askstring("Input", prompt))
            return value
        except (ValueError, TypeError):
            messagebox.showerror("Invalid input", "Please enter an integer.")

def input_float(prompt):
    while True:
        try:
            value = float(simpledialog.askstring("Input", prompt))
            return value
        except (ValueError, TypeError):
            messagebox.showerror("Invalid input", "Please enter a float number.")

def add_student(students):
    student_code = input_integer("Enter student code: ")
    student_name = simpledialog.askstring("Input", "Enter student name: ")
    total_score = input_float("Enter total score: ")
    students.append({'student_code': student_code, 'student_name': student_name, 'total_score': total_score})
    save_students(students)
    messagebox.showinfo("Info", "Student added successfully.")

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

def delete_student(students):
    student_code = input_integer("Enter student code to delete: ")
    for student in students:
        if student['student_code'] == student_code:
            students.remove(student)
            save_students(students)
            messagebox.showinfo("Info", "Student deleted successfully.")
            return
    messagebox.showerror("Error", "Student not found.")

def search_students(students):
    criterion = simpledialog.askstring("Input", "Search by (code/name/score): ").strip().lower()
    query = simpledialog.askstring("Input", "Enter search value: ").strip()
    results = []

    if criterion == 'code':
        try:
            query = int(query)
            results = [student for student in students if student['student_code'] == query]
        except ValueError:
            messagebox.showerror("Error", "Invalid student code.")
            return
    elif criterion == 'name':
        results = [student for student in students if query.lower() in student['student_name'].lower()]
    elif criterion == 'score':
        try:
            query = float(query)
            results = [student for student in students if student['total_score'] == query]
        except ValueError:
            messagebox.showerror("Error", "Invalid score.")
            return
    else:
        messagebox.showerror("Error", "Invalid search criterion.")
        return

    if results:
        result_text = "\n".join(f"Code: {student['student_code']}, Name: {student['student_name']}, Score: {student['total_score']}" for student in results)
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", "No matching students found.")

def print_students(students):
    result_text = "\n".join(f"Code: {student['student_code']}, Name: {student['student_name']}, Score: {student['total_score']}" for student in students)
    messagebox.showinfo("All Students", result_text)

def main():
    students = load_students()

    root = tk.Tk()
    root.title("Classroom Management_Bui Nhat Minh_21021341")
    root.geometry("300x250")
    
    style = ttk.Style(root)
    style.theme_use("clam")

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

    frame = ttk.Frame(root, padding="10")
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    ttk.Button(frame, text="Add Student", command=on_add).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(frame, text="Edit Student", command=on_edit).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(frame, text="Delete Student", command=on_delete).grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(frame, text="Search Student", command=on_search).grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(frame, text="Print All Students", command=on_print).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    ttk.Button(frame, text="Exit", command=root.quit).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
