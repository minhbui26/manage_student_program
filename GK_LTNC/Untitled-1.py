import csv
with open('Danh_sach.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)