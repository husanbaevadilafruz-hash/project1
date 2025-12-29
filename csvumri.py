# import csv
# with open('grades.csv', newline='', encoding='utf-8') as fid:
#     reader=csv.DictReader(fid)
#     for row in reader:
#         print(row)

import csv

with open("grades.csv", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)