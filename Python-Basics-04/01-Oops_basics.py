#class and object
class Students:
    subject = "Python"
    college = "IPU College"

stu1=Students()
print(stu1)
print(stu1.subject)
print(stu1.college) 

#attributes and methods
# In Python, an attribute is a variable or value associated with an object or a class, accessed using "dot notation"

# In Python, a method is a function that is "bound" to an object or class. While a standard function is defined independently, a method is defined within a class and typically operates on the data (attributes) contained in that class. 
class Student:
    subject = "Python"
    college = "IPU College"
    year="Final Year"

    def function1(self):
        print("This is a method of Student class")
stud1=Student()
print(stud1.subject)
print(stud1.college)
print(stud1.year)
stud1.function1()       

