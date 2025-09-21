import json

file_path = "C:/Users/A.R/Desktop/created_json_file.json"

try:
    # Open JSON file in read mode ("r")
    with open(file_path, "r") as file:
        content = json.load(file)   # Converts JSON data into a Python dictionary
        print(content)              # Full dictionary output
        # Example: print(content["name"]) to access specific keys

# Handles missing file error
except FileNotFoundError:
    print("That file was not found")

# Handles permission error (file exists but cannot be opened)
except PermissionError:
    print("You do not have permission to read that file")
