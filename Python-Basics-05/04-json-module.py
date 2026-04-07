import json

# Python dict to JSON string (dumps)
data = {"name": "Aisha", "city": "Delhi", "marks": [85, 90, 92]}
json_string = json.dumps(data)
print(json_string)  # '{"name": "Aisha", "city": "Delhi", "marks": [85, 90, 92]}'

# JSON string to Python dict (loads)
json_data = '{"name": "John", "age": 25}'
python_obj = json.loads(json_data)
print(python_obj["name"])  # John

# Write JSON to file
data = {"name": "John", "age": 25, "marks": [85, 90, 92]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # indent makes it pretty

# Read JSON from file
with open("data.json", "r") as f:
    data = json.load(f)
    print(data["name"])  # John

# Complete example: Save and load student data
students = [
    {"name": "Aisha", "marks": 85},
    {"name": "John", "marks": 92}
]

# Save
with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

# Load and process
with open("students.json", "r") as f:
    students = json.load(f)
    avg_marks = sum(s["marks"] for s in students) / len(students)
    print(f"Average marks: {avg_marks}")