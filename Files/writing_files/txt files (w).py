txt_data = "I like pizza!"

# Absolute paths to store files on Desktop
file_path1 = "C:/Users/A.R/Desktop/created_txt_file1.txt"
file_path2 = "C:/Users/A.R/Desktop/created_txt_file2.txt"
file_path3 = "C:/Users/A.R/Desktop/created_txt_file3.txt"
file_path4 = "C:/Users/A.R/Desktop/created_txt_file4.txt"

# File modes:
# "w" = Write (creates new file or overwrites existing)
# "x" = Exclusive creation (error if file exists)
# "a" = Append (adds to file, creates if deosn't exist)


# --------- 1. Basic writing (overwrite/create new) --------- #
with open(file_path1, "w") as file:
    file.write(txt_data)
print(f"'{file_path1}' created (or overwritten)\n")


# --------- 2. Writing with error handling (exclusive creation) --------- #
try:
    with open(file_path2, "x") as file:
        file.write(txt_data)
    print(f"'{file_path2}' created exclusively\n")
except FileExistsError:
    print(f"'{file_path2}' already exists! Skipped.\n")


# --------- 3. Writing and then appending each run --------- #
with open(file_path3, "a") as file:
    file.write("\n" + txt_data)
print(f"'{file_path3}' created/appended\n")


# --------- 4. Writing list data line by line --------- #
employees = ["Eugene", "Spongebob", "Squidward", "Patrick"]

with open(file_path4, "w") as file:
    for employee in employees:
        file.write(employee + "\n")
print(f"'{file_path4}' created with employee list\n")
