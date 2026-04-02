# Output and Input in Python

## Output using print()

`print()` function is used to display output on the screen.

### Examples

print("Hello World")
print(3.14)
print(2 + 3)
print("hello world", "from PRIME")

- Strings inside quotes print as it is
- Each print statement shows output on a new line

---

## Python Character Set

Python supports:

- English letters (a-z, A-Z)
- Digits (0-9)
- Special symbols (+, -, *, /, %)
- Whitespaces and escape characters (\n, \t)
- ASCII and Unicode characters

---

## Input using input()

`input()` is used to take user input during program execution.

By default, input is stored as **string**.

### Example

name = input("Enter name: ")
print(name)
print(type(name))

### Type Casting with Input

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

### Practice: Average of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
avg = (a + b) / 2
print("Average =", avg)