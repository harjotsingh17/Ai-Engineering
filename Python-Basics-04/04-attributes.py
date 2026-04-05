# attributes:
# In Python, an attribute is a variable or value associated with an object or a class, accessed using "dot notation"
# class and object
     
class Student:
    college_name = "ABC college" #class
    PI = 3.14 #class

    def __init__(self, name, gpa):
        self.name = name #instance
        self.gpa = gpa
        self.PI = 3.14 #instance

stu1 = Student("Rahul", 9.2)
print(stu1.name,stu1.gpa) #instance

print(Student.PI)