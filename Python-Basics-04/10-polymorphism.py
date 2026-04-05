# polymorphism:operator overloading parent class method is used by child class in different way that is why it is called polymorphism
class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()

# duck typing(no inheritance): if it looks like a duck and quacks like a duck, then it is a duck
class Teacher():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")

t1 = Teacher()
t1.get_designation()