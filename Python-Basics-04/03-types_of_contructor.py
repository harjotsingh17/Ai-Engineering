# Types of Constructor in Python
# 1. Default Constructor: A default constructor is a constructor that takes no parameters and initializes the object with default values. If you do not define any constructor in a class, Python automatically provides a default constructor.
class Student:
    def __init__(self):
        self.name = "Unknown"
        self.cgpa = 0.0
s1=Student()
print(s1.name)  # Output: Unknown
print(s1.cgpa)  # Output: 0.0
# 2. Parameterized Constructor: A parameterized constructor is a constructor that takes parameters to initialize the object with specific values.        
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa


s1=Student("Harjot", 8.5)
s2=Student("Singh", 9.0)
s3=Student("YASH", 8.7)

print(s1.name)
print(s2.name)
print(s3.name)

print(s1.cgpa)
print(s2.cgpa)
print(s3.cgpa)