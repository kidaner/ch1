import csv

file = open("kids.txt")

file_csv = csv.reader(file)

for x in file_csv:
    name, number, city = x
    print(f"{name}, {number}, {city}")

file.close()
