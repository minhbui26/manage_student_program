# bản chính để nộp
# để chạy chương trình hãy tải thư viện pyqt5 chạy câu lệnh sau ở terminal
# pip install pyqt5

import csv
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
import sys

CSV_FILE = 'student.csv'  # Tên file CSV để lưu dữ liệu học sinh


class StudentManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Classroom Management Program_BuiNhatMinh_21021341")
        self.setGeometry(100, 100, 800, 600)

        self.students = self.load_students()  # Tải dữ liệu học sinh từ file CSV

        self.initUI()  # Khởi tạo giao diện người dùng

    def load_students(self):
        students = {}
        with open(CSV_FILE,encoding='utf-8', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_code = int(row['student_code'])
                    students[student_code] = {
                        'student_name': row['student_name'],
                        'total_score': float(row['total_score'])
                    }
        return students

    def save_students(self):
        with open(CSV_FILE, mode='w', newline='') as file:
            fieldnames = ['student_code', 'student_name', 'total_score']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for code, data in self.students.items():
                writer.writerow(
                    {'student_code': code, 'student_name': data['student_name'], 'total_score': data['total_score']})

    def initUI(self):
        self.note_label = QtWidgets.QLabel(self)
        self.note_label.setText(
            "Note:\n1. Student code must include 8 numbers.\n2. Total score is less than 4.0.\n3. In the Edit student section, please enter the correct student code to change the name and total score.")
        self.note_label.setStyleSheet("color: red;")
        self.note_label.setGeometry(10, 10, 800, 60)

        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setGeometry(10, 80, 780, 510)

        self.add_tab = QtWidgets.QWidget()
        self.edit_tab = QtWidgets.QWidget()
        self.delete_tab = QtWidgets.QWidget()
        self.search_tab = QtWidgets.QWidget()
        self.print_tab = QtWidgets.QWidget()

        self.tab_widget.addTab(self.add_tab, "Add Student")
        self.tab_widget.addTab(self.edit_tab, "Edit Student")
        self.tab_widget.addTab(self.delete_tab, "Delete Student")
        self.tab_widget.addTab(self.search_tab, "Search Student")
        self.tab_widget.addTab(self.print_tab, "Print All Students")

        self.initAddTab()  # Khởi tạo tab thêm học sinh
        self.initEditTab()  # Khởi tạo tab chỉnh sửa học sinh
        self.initDeleteTab()  # Khởi tạo tab xóa học sinh
        self.initSearchTab()  # Khởi tạo tab tìm kiếm học sinh
        self.initPrintTab()  # Khởi tạo tab in danh sách học sinh

    def initAddTab(self):
        layout = QtWidgets.QVBoxLayout()

        self.add_student_code_label = QtWidgets.QLabel("Student Code (8 numbers):")
        self.add_student_code_input = QtWidgets.QLineEdit()

        self.add_student_name_label = QtWidgets.QLabel("Student Name:")
        self.add_student_name_input = QtWidgets.QLineEdit()

        self.add_total_score_label = QtWidgets.QLabel("Total Score (not greater than 4):")
        self.add_total_score_input = QtWidgets.QLineEdit()

        self.add_student_button = QtWidgets.QPushButton("Add Student")
        self.add_student_button.clicked.connect(self.add_student)

        layout.addWidget(self.add_student_code_label)
        layout.addWidget(self.add_student_code_input)
        layout.addWidget(self.add_student_name_label)
        layout.addWidget(self.add_student_name_input)
        layout.addWidget(self.add_total_score_label)
        layout.addWidget(self.add_total_score_input)
        layout.addWidget(self.add_student_button)

        self.add_tab.setLayout(layout)

    def add_student(self):
        student_code = self.add_student_code_input.text()
        if not student_code.isdigit() or len(student_code) != 8:
            QMessageBox.critical(self, "Error",
                                 "Student code must be exactly 8 numbers.")  # Kiểm tra mã học sinh phải là 8 số
            return
        student_code = int(student_code)
        student_name = self.add_student_name_input.text()
        try:
            total_score = float(self.add_total_score_input.text())
            if total_score > 4:
                QMessageBox.critical(self, "Error",
                                     "Total score cannot be greater than 4.")  # Kiểm tra điểm tổng không được lớn hơn 4
                return
        except ValueError:
            QMessageBox.critical(self, "Error", "Total score must be a number.")  # Kiểm tra điểm tổng phải là số
            return
        if student_code in self.students:
            QMessageBox.critical(self, "Error", "Student code already exists.")  # Kiểm tra mã học sinh phải là duy nhất
            return
        self.students[student_code] = {'student_name': student_name, 'total_score': total_score}
        self.save_students()
        QMessageBox.information(self, "Success", "Student added successfully.")  # Thông báo thêm học sinh thành công
        self.add_student_code_input.clear()
        self.add_student_name_input.clear()
        self.add_total_score_input.clear()

    def initEditTab(self):
        layout = QtWidgets.QVBoxLayout()

        self.edit_student_code_label = QtWidgets.QLabel("Student Code (8 numbers):")
        self.edit_student_code_input = QtWidgets.QLineEdit()

        self.edit_student_name_label = QtWidgets.QLabel("Student Name:")
        self.edit_student_name_input = QtWidgets.QLineEdit()

        self.edit_total_score_label = QtWidgets.QLabel("Total Score (not greater than 4):")
        self.edit_total_score_input = QtWidgets.QLineEdit()

        self.edit_student_button = QtWidgets.QPushButton("Edit Student")
        self.edit_student_button.clicked.connect(self.edit_student)

        layout.addWidget(self.edit_student_code_label)
        layout.addWidget(self.edit_student_code_input)
        layout.addWidget(self.edit_student_name_label)
        layout.addWidget(self.edit_student_name_input)
        layout.addWidget(self.edit_total_score_label)
        layout.addWidget(self.edit_total_score_input)
        layout.addWidget(self.edit_student_button)

        self.edit_tab.setLayout(layout)

    def edit_student(self):
        student_code = self.edit_student_code_input.text()
        if not student_code.isdigit() or len(student_code) != 8:
            QMessageBox.critical(self, "Error","Student code must be exactly 8 numbers.")  # Kiểm tra mã học sinh phải là 8 số
            return
        student_code = int(student_code)
        student_name = self.edit_student_name_input.text()
        try:
            total_score = float(self.edit_total_score_input.text())
            if total_score > 4:
                QMessageBox.critical(self, "Error","Total score cannot be greater than 4.")  # Kiểm tra điểm tổng không được lớn hơn 4
                return
        except ValueError:
            QMessageBox.critical(self, "Error", "Total score must be a number.")  # Kiểm tra điểm tổng phải là số
            return
        if student_code not in self.students:
            QMessageBox.critical(self, "Error", "Student code not found.")  # Kiểm tra mã học sinh phải tồn tại
            return
        self.students[student_code] = {'student_name': student_name, 'total_score': total_score}
        self.save_students()
        QMessageBox.information(self, "Success",
                                "Student edited successfully.")  # Thông báo chỉnh sửa học sinh thành công
        self.edit_student_code_input.clear()
        self.edit_student_name_input.clear()
        self.edit_total_score_input.clear()

    def initDeleteTab(self):
        layout = QtWidgets.QVBoxLayout()

        self.delete_student_code_label = QtWidgets.QLabel("Student Code (8 numbers):")
        self.delete_student_code_input = QtWidgets.QLineEdit()

        self.delete_student_button = QtWidgets.QPushButton("Delete Student")
        self.delete_student_button.clicked.connect(self.delete_student)

        layout.addWidget(self.delete_student_code_label)
        layout.addWidget(self.delete_student_code_input)
        layout.addWidget(self.delete_student_button)

        self.delete_tab.setLayout(layout)

    def delete_student(self):
        student_code = self.delete_student_code_input.text()
        if not student_code.isdigit() or len(student_code) != 8:
            QMessageBox.critical(self, "Error",
                                 "Student code must be exactly 8 numbers.")  # Kiểm tra mã học sinh phải là 8 số
            return
        student_code = int(student_code)
        if student_code in self.students:
            del self.students[student_code]
            self.save_students()
            QMessageBox.information(self, "Success",
                                    f"Student with code {student_code} has been deleted.")  # Thông báo xóa học sinh thành công
        else:
            QMessageBox.critical(self, "Error", "Student code not found.")  # Kiểm tra mã học sinh phải tồn tại
        self.delete_student_code_input.clear()

    def initSearchTab(self):
        layout = QtWidgets.QVBoxLayout()

        self.search_student_code_label = QtWidgets.QLabel("Student Code (8 numbers):")
        self.search_student_code_input = QtWidgets.QLineEdit()

        self.search_student_name_label = QtWidgets.QLabel("Student Name:")
        self.search_student_name_input = QtWidgets.QLineEdit()

        self.search_total_score_label = QtWidgets.QLabel("Total Score:")
        self.search_total_score_input = QtWidgets.QLineEdit()

        self.search_student_button = QtWidgets.QPushButton("Search Student")
        self.search_student_button.clicked.connect(self.search_student)

        self.search_table_widget = QtWidgets.QTableWidget()
        self.search_table_widget.setColumnCount(3)
        self.search_table_widget.setHorizontalHeaderLabels(["Student Code", "Student Name", "Total Score"])
        self.search_table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        layout.addWidget(self.search_student_code_label)
        layout.addWidget(self.search_student_code_input)
        layout.addWidget(self.search_student_name_label)
        layout.addWidget(self.search_student_name_input)
        layout.addWidget(self.search_total_score_label)
        layout.addWidget(self.search_total_score_input)
        layout.addWidget(self.search_student_button)
        layout.addWidget(self.search_table_widget)

        self.search_tab.setLayout(layout)

    def search_student(self):
        student_code = self.search_student_code_input.text()
        student_name = self.search_student_name_input.text().lower()
        total_score = self.search_total_score_input.text()

        self.search_table_widget.setRowCount(0)
        results = []

        if student_code.isdigit() and len(student_code) == 8:
            student_code = int(student_code)
            if student_code in self.students:
                results.append((student_code, self.students[student_code]))

        if student_name:
            for code, data in self.students.items():
                if student_name in data['student_name'].lower():
                    results.append((code, data))

        if total_score:
            try:
                total_score = float(total_score)
                for code, data in self.students.items():
                    if data['total_score'] == total_score:
                        results.append((code, data))
            except ValueError:
                QMessageBox.critical(self, "Error", "Total score must be a number.")  # Kiểm tra điểm tổng phải là số
                return

        if results:
            self.search_table_widget.setRowCount(len(results))
            for row, (code, data) in enumerate(results):
                self.search_table_widget.setItem(row, 0, QTableWidgetItem(str(code)))
                self.search_table_widget.setItem(row, 1, QTableWidgetItem(data['student_name']))
                self.search_table_widget.setItem(row, 2, QTableWidgetItem(str(data['total_score'])))
        else:
            QMessageBox.critical(self, "Error",
                                 "No matching student found.")  # Thông báo không tìm thấy học sinh phù hợp

        self.search_student_code_input.clear()
        self.search_student_name_input.clear()
        self.search_total_score_input.clear()

    def initPrintTab(self):
        layout = QtWidgets.QVBoxLayout()

        self.print_button = QtWidgets.QPushButton("Print All Students")
        self.print_button.clicked.connect(self.print_all_students)

        self.table_widget = QtWidgets.QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Student Code", "Student Name", "Total Score"])
        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        layout.addWidget(self.print_button)
        layout.addWidget(self.table_widget)

        self.print_tab.setLayout(layout)

    def print_all_students(self):
        self.table_widget.setRowCount(len(self.students))
        self.table_widget.clearContents()
        for row, (code, data) in enumerate(self.students.items()):
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(code)))
            self.table_widget.setItem(row, 1, QTableWidgetItem(data['student_name']))
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(data['total_score'])))

def main():
    app = QApplication(sys.argv)
    window = StudentManagementApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
