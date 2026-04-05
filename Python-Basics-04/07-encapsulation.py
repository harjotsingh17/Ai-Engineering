# encapsulation in python: public, protected and private attributes

class BankAccount:
    def __init__(self, name, balance):
        self.name = name#public attribute
        self._balance = balance  # Protected attribute
    def get_balance(self): #getter method to access protected attribute
        return self._balance 
    def set_balance(self, amount):  #setter method to modify protected attribute
        self._balance = amount

acc1=BankAccount("Harjot", 1000)
acc1.set_balance(1500)
print(acc1.name) #public attribute can be accessed directly    
print(acc1.get_balance()) #accessing protected attribute using getter method 
