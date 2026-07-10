import csv
with open("name.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
'''
-------Erases everything from csv file-----------
with open("name.csv","w",newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["name","age","city"])
    writer.writerow(["Alice",25,"New York"])
    writer.writerow(["Bob",30,"Los Angeles"])
'''
with open("name.csv","a",newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["name","age","city"])
    writer.writerow(["Alice",25,"New York"])
    writer.writerow(["Bob",30,"Los Angeles"])


