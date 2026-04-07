# Basic try-except
try:
    x = 10 / 0  # ZeroDivisionError
except:
    print("Error occurred!")

# Specific exceptions
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Multiple exceptions
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")

# try-except-else-finally
try:
    f = open("data.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")  # Runs only if no exception
finally:
    print("Cleanup done.")  # Always runs

# Delete file
import os
try:
    os.remove("data.txt")  # Delete file
    print("File deleted")
except FileNotFoundError:
    print("File doesn't exist")