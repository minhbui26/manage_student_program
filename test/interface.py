import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

CSV_FILE = 'class_list.csv'

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
        print(f"{CSV_FILE} not found, starting with a new emty class list.")
    return students

def save_students(students):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ['student_code', 'student_name', 'total_score']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for code, data in students.items():
            writer.writerow({'student_code': code, 'student_name': data['student_name'], 'total_score': data['total_score']})

def add_student():
    student_code = entry_student_code.get()
    if not student_code.isdigit() or len(student_code) != 8:
        messagebox.showerror("Error", "Student code must be exactly 8 digits.")
        return
    student_code = int(student_code)
    student_name = entry_student_name.get()
    total_score = float(entry_total_score.get())
    if total_score > 4:
        messagebox.showerror("Error", "Total score cannot be greater than 4.")
        return
    if student_code in students:
        messagebox.showerror("Error", "Student code already exists.")
        return
    students[student_code] = {'student_name': student_name, 'total_score': total_score}
    save_students(students)
    messagebox.showinfo("Success", "Student added successfully.")

def edit_student():
    student_code = entry_student_code_edit.get()
    if not student_code.isdigit() or len(student_code) != 8:
        messagebox.showerror("Error", "Student code must be exactly 8 digits.")
        return
    student_code = int(student_code)
    student_name = entry_student_name_edit.get()
    total_score = float(entry_total_score_edit.get())
    if total_score > 4:
        messagebox.showerror("Error", "Total score cannot be greater than 4.")
        return
    if student_code not in students:
        messagebox.showerror("Error", "Student code not found.")
        return
    students[student_code] = {'student_name': student_name, 'total_score': total_score}
    save_students(students)
    messagebox.showinfo("Success", "Student edited successfully.")

def delete_student():
    student_code = entry_student_code_delete.get()
    if not student_code.isdigit() or len(student_code) != 8:
        messagebox.showerror("Error", "Student code must be exactly 8 digits.")
        return
    student_code = int(student_code)
    if student_code in students:
        del students[student_code]
        save_students(students)
        messagebox.showinfo("Success", f"Student with code {student_code} has been deleted.")
    else:
        messagebox.showerror("Error", "Student code not found.")

def search_student_by_code():
    student_code = entry_student_code_search.get()
    if not student_code.isdigit() or len(student_code) != 8:
        messagebox.showerror("Error", "Student code must be exactly 8 digits.")
        return
    student_code = int(student_code)
    if student_code in students:
        student_info = students[student_code]
        messagebox.showinfo("Student Info", f"Student Code: {student_code}\nStudent Name: {student_info['student_name']}\nTotal Score: {student_info['total_score']}")
    else:
        messagebox.showerror("Error", "Student code not found.")

def print_all_students():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Student Code\tStudent Name\tTotal Score\n")
    output_text.insert(tk.END, "-"*50 + "\n")
    for code, data in students.items():
        output_text.insert(tk.END, f"{code}\t{data['student_name']}\t{data['total_score']}\n")

window = tk.Tk()
window.title("Classroom Management Program")

students = load_students()

note_label = tk.Label(window, text="Note:\n1. Student code must include 8 numbers\n2. Total score is less than 4\n3. In the student information change section, \nplease enter the correct student code to change the name and total score", fg="red")
note_label.pack(padx=10, pady=5)

frame_add = tk.LabelFrame(window, text="Add Student")
frame_add.pack(padx=10, pady=5, fill="both")

tk.Label(frame_add, text="Student Code (8 digits):").grid(row=0, column=0, sticky="w")
entry_student_code = tk.Entry(frame_add)
entry_student_code.grid(row=0, column=1)

tk.Label(frame_add, text="Student Name:").grid(row=1, column=0, sticky="w")
entry_student_name = tk.Entry(frame_add)
entry_student_name.grid(row=1, column=1)

tk.Label(frame_add, text="Total Score (not greater than 4):").grid(row=2, column=0, sticky="w")
entry_total_score = tk.Entry(frame_add)
entry_total_score.grid(row=2, column=1)

btn_add_student = tk.Button(frame_add, text="Add Student", command=add_student)
btn_add_student.grid(row=3, columnspan=2, pady=5)

frame_edit = tk.LabelFrame(window, text="Edit Student")
frame_edit.pack(padx=10, pady=5, fill="both")

tk.Label(frame_edit, text="Student Code (8 digits):").grid(row=0, column=0, sticky="w")
entry_student_code_edit = tk.Entry(frame_edit)
entry_student_code_edit.grid(row=0, column=1)

tk.Label(frame_edit, text="Student Name:").grid(row=1, column=0, sticky="w")
entry_student_name_edit = tk.Entry(frame_edit)
entry_student_name_edit.grid(row=1, column=1)

tk.Label(frame_edit, text="Total Score (not greater than 4):").grid(row=2, column=0, sticky="w")
entry_total_score_edit = tk.Entry(frame_edit)
entry_total_score_edit.grid(row=2, column=1)

btn_edit_student = tk.Button(frame_edit, text="Edit Student", command=edit_student)
btn_edit_student.grid(row=3, columnspan=2, pady=5)

frame_delete = tk.LabelFrame(window, text="Delete Student")
frame_delete.pack(padx=10, pady=5, fill="both")

tk.Label(frame_delete, text="Student Code (8 digits):").grid(row=0, column=0, sticky="w")
entry_student_code_delete = tk.Entry(frame_delete)
entry_student_code_delete.grid(row=0, column=1)

btn_delete_student = tk.Button(frame_delete, text="Delete Student", command=delete_student)
btn_delete_student.grid(row=1, columnspan=2, pady=5)

frame_search = tk.LabelFrame(window, text="Search Student")
frame_search.pack(padx=10, pady=5, fill="both")

tk.Label(frame_search, text="Student Code (8 digits):").grid(row=0, column=0, sticky="w")
entry_student_code_search = tk.Entry(frame_search)
entry_student_code_search.grid(row=0, column=1)

btn_search_student = tk.Button(frame_search, text="Search Student", command=search_student_by_code)
btn_search_student.grid(row=1, columnspan=2, pady=5)

frame_print = tk.LabelFrame(window, text="Print All Students")
frame_print.pack(padx=10, pady=5, fill="both")

btn_print_all_students = tk.Button(frame_print, text="Print All Students", command=print_all_students)
btn_print_all_students.pack(pady=5)

output_text = scrolledtext.ScrolledText(frame_print, width=50, height=10)
output_text.pack(padx=10, pady=5)

window.mainloop()
