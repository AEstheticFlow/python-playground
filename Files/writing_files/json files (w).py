import json

# Data to be saved as JSON
employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "Cook"
}

# Output file path
file_path = "C:/Users/A.R/Desktop/created_json_file.json"

# Write JSON data with indentation (readable formatting)
with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)
print(f"JSON file '{file_path}' created successfully")
