import os

# --------- EXAMPLE 1: File inside workspace --------- #
file_path = "Files/file_detection/test.txt"  # Relative path within project

if os.path.exists(file_path):                # Check if path exists
    print(f"'{file_path}' exists")           # Check if it's a file
    if os.path.isfile(file_path):
        print("→ It's a file\n")
    elif os.path.isdir(file_path):           # Check if it's a directory
        print("→ It's a directory\n")
else:
    print(f"'{file_path}' does NOT exist\n")


# --------- EXAMPLE 2: Directory inside workspace --------- #
file_path2 = "Files/file_detection"          # Using the containing directory itself

if os.path.exists(file_path2):
    print(f"'{file_path2}' exists")
    if os.path.isfile(file_path2):
        print("→ It's a file\n")
    elif os.path.isdir(file_path2):
        print("→ It's a directory\n")
else:
    print(f"'{file_path2}' does NOT exist\n")


# --------- EXAMPLE 3: File on desktop (absolute path) --------- #
file_path3 = "C:/Users/A.R/Desktop/test3.txt"

if os.path.exists(file_path3):
    print(f"'{file_path3}' exists")
    if os.path.isfile(file_path3):
        print("→ It's a file\n")
    elif os.path.isdir(file_path3):
        print("→ It's a directory\n")
else:
    print(f"'{file_path3}' does NOT exist\n")


# https://www.youtube.com/watch?v=EReeJSaU0Og&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=70