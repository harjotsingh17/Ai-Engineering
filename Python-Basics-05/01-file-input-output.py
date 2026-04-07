# file i/o
# 1. Reading from a file
# 2. Writing to a file  
# 3. Appending to a file
# 4. Working with file paths
# 5. Handling file exceptions
# 1. Reading from a file
# open() function is used to open a file in Python. It takes two arguments: the file name and the mode (e.g., 'r' for reading, 'w' for writing, 'a' for appending). The read() method is used to read the contents of the file.
# Open file in read mode (default) - errors if file doesn't exist
f = open("D:\Ai Engineering\Python-Basics-05\example.txt", "r")
content = f.read()  # Read entire file as string
print(content)
f.close()

# Read one line at a time
f = open("D:\Ai Engineering\Python-Basics-05\example.txt", "r")
line1 = f.readline()  # First line
line2 = f.readline()  # Second line
print(line1, line2)
f.close()

# Read all lines into list
f = open("D:\Ai Engineering\Python-Basics-05\example.txt", "r")
lines = f.readlines()  # Returns list of lines
print(lines)
f.close()

# Write mode - overwrites file
f = open("D:\Ai Engineering\Python-Basics-05\example.txtt", "w")
f.write("Hello students!\n")  # Write string
f.close()

# Append mode - adds to end
f = open("D:\Ai Engineering\Python-Basics-05\example.txt", "a")
f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])  # Write multiple lines
f.close()

# BETTER: Use 'with' statement (auto-closes file)
with open("D:\Ai Engineering\Python-Basics-05\example.txt", "r") as f:
    content = f.read()
    print(content)

# Common modes summary
modes = {
    "r": "Read (default)",
    "w": "Write (overwrite)",
    "a": "Append",
    "r+": "Read+Write",
    "w+": "Write+Read (overwrite)",
    "a+": "Append+Read"
}
