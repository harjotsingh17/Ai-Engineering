# __init__ method is a special function used as a constructor to initialize a new object's state. It is a "dunder" (double underscore) method that runs automatically when a class is instantiated.
class Student:
    def __init__(self, name):
        self.name = name

s1=Student("Harjot")
s2=Student("Singh")

s3=Student("YASH")

print(s1.name)
print(s2.name)
print(s3.name)