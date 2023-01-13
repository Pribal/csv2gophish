import csv

def check_extension(file, extension):
    file_array = file.split(".")
    if(len(file_array) > 1):
        if(file_array[1] != extension):
            return ".".join([file_array[0], extension])
        else:
            return file
    else:
        return ".".join([file_array[0], extension])

original_file = input("Name of file: ")
original_file = check_extension(original_file, "csv")
bool_header = input("Header row in file? (y/n): ")

match(bool_header):
    case "y":
        bool_header = True
    case "n":
        bool_header = False


indexes = input("Indexes of the columns (order: First Name, Last Name, Position, Email)(separate with ,): ").split(",")

final_file_name = input("Name of the created file: ")
final_file_name = check_extension(final_file_name, "csv")

with open(original_file, encoding="utf-8") as csv_original_file:
    reader = csv.reader(csv_original_file, delimiter=";")
    data = []
    for index, row in enumerate(reader):
        if(bool_header and index == 0):
            continue
        user = []
        for index in indexes:
            user.append(row[int(index)])
        data.append(user)

with open(final_file_name, "w", newline="", encoding="utf-8") as new_file:
    writer = csv.writer(new_file, delimiter=",")
    writer.writerow(["First Name","Last Name","Position","Email"])
    for row in data:
        writer.writerow(row)


