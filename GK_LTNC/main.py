import csv

with open('Danh_sach.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
