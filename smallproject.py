import csv

# Ask for number of students
num = int(input("How many students do you want to enter? "))

# Open CSV file for writing
with open("smallproject.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["Name", "Age", "Grade"])

    # Input student details
    for i in range(num):
        print(f"\nEnter details for Student {i + 1}")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")

        writer.writerow([name, age, grade])

print("\nStudent records saved successfully!")

# Read the CSV file
print("\nReading Student Records:\n")

with open("smallproject.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)