import json
import os

# 1. Create and save data
data = {
    "students": [
        {"name": "Aisha", "city": "Delhi", "marks": [85, 90, 92]},
        {"name": "John", "city": "Mumbai", "marks": [78, 88, 91]}
    ]
}

# Save to JSON
with open("class_data.json", "w") as f:
    json.dump(data, f, indent=2)

# 2. Read and process with error handling
try:
    with open("class_data.json", "r") as f:
        data = json.load(f)
        
    # List comprehension: Get all marks
    all_marks = [mark for student in data["students"] for mark in student["marks"]]
    avg = sum(all_marks) / len(all_marks)
    
    print(f"All marks: {all_marks}")
    print(f"Average: {avg:.1f}")
    
except FileNotFoundError:
    print("JSON file not found!")
except json.JSONDecodeError:
    print("Invalid JSON format!")
finally:
    print("Processing complete.")

# 3. Delete file
try:
    os.remove("class_data.json")
    print("Temp file cleaned up.")
except:
    pass