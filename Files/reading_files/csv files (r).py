import csv

file_path = "C:/Users/A.R/Desktop/created_csv_file.csv"

try:
    # Open CSV file in read mode ("r")
    with open(file_path, "r") as file:
        content = csv.reader(file)  # Reads CSV as an iterable of rows (each row is a list)
        
        for line in content:
            print(line)  # Prints each row as a list
            # Example: print(line[0]) for the first column value

# Handles missing file error
except FileNotFoundError:
    print("That file was not found")

# Handles permission error (file exists but cannot be accessed)
except PermissionError:
    print("You do not have permission to read that file")


# https://www.youtube.com/watch?v=GWBWQnWNWBI&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=74
