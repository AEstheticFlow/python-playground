file_path = "C:/Users/A.R/Desktop/created_txt_file1.txt"

try:
    # Open file in read mode ("r")
    with open(file_path, "r") as file:
        content = file.read()  # Reads entire file as a single string
        print(content)

# Handles case where the file does not exist
except FileNotFoundError:
    print("That file was not found")

# Handles case where file exists but cannot be accessed (permissions issue)
except PermissionError:
    print("You do not have permission to read that file")
