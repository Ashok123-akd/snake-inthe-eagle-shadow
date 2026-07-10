#______________USing dictionary with csv__________________________________

import csv
student = {
    "name": "Ashok",
    "age": 29,
    "city": "Italy"
}

with open("student.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerow(student)