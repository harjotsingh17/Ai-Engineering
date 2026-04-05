# inheritance: reusing attributes and methods of parent class in child class
# parent class: base class or super class
# child class: derived class or sub class




class Employees:
    start_time = "9:00 am"
    end_time = "5:00 pm"

    def change_time(self, end):
        self.end_time = end
class Manager(Employees):
    def __init__(self):
        self.name = "Harjot"
        self.salary = 50000
m1=Manager()
m1.change_time("6:00 pm")
print(m1.name)
print(m1.salary)
print(m1.start_time)
print(m1.end_time)

#types of inheritance: single, multilevel, multiple
#eg of multilevel inheritance: Employee is parent class, AdminStaff is child class of Employee and Accountant is child class of AdminStaff
class Employee:
    start_time = "10am"
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant (AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant(25_000, "CA")

print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)

#eg of multiple inheritance: AdminStaff is child class of Employee and HRStaff is child class of Employee
class Employee:
    start_time = "10am"
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role
class HRStaff(Employee):
    def __init__(self, department):
        self.department = department
class Manager(AdminStaff, HRStaff):
    def __init__(self, name, role, department):
        AdminStaff.__init__(self, role)
        HRStaff.__init__(self, department)
        self.name = name
m1 = Manager("Harjot", "Admin", "HR")
print(m1.name, m1.role, m1.department, m1.start_time, m1.end_time)

