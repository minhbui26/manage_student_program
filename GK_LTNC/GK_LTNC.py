import csv

class Student:
    def __init__(self, ma_sv, name, position, grade, gender):
        self.ma_sv = ma_sv
        self.name = name
        self.position = position
        self.grade = grade
        self.gender = gender

class Class:
    def __init__(self, filename):
        self.students = []
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.students.append(Student(row['id'], row['name'], row['position'], row['grade'], row['gender']))
                
    def find_student(self, **kwargs):
        result = []
        for student in self.students:
            for key, value in kwargs.items():
                if getattr(student, key) != value:
                    break
            else:
                result.append(student)
        return result
        
    def sort_students(self, criteria):
        if criteria == 'position':
            self.students.sort(key=lambda x: x.position)
        elif criteria == 'grade':
            self.students.sort(key=lambda x: x.grade)
        elif criteria == 'gender':
            self.students.sort(key=lambda x: x.gender)
            
    def print_students(self):
        for student in self.students:
            print(f"{student.name} - {student.position} - {student.grade} - {student.gender}", end=' ')
