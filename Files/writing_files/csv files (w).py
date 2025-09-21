import csv

# Data to be written to the CSV file
employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]

file_path = "C:/Users/A.R/Desktop/created_csv_file.csv"

# 'newline=""' prevents blank lines from appearing between rows on Windows
with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)

print(f"CSV file '{file_path}' was created")


# https://www.youtube.com/watch?v=1IYrmTTKOoI&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=71