# methods : instance, class and static methods
# isinstance() is a built-in function in Python that checks if an object is an instance of a specified class or a subclass thereof.
class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

l1.get_info()

# class methods: A class method is a method that is bound to the class and not the instance of the class. It can modify the class state that applies across all instances of the class. Class methods are defined using the @classmethod decorator and take cls as the first parameter, which refers to the class itself.
class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type} {cls.RAM}")

    def get_info(self): #instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

l1 = Laptop("16gb", "512gb")

l1.get_storage_type()


# static methods: A static method is a method that belongs to a class rather than an instance of the class. It does not have access to the instance (self) or class (cls) variables and is defined using the @staticmethod decorator. Static methods are used for utility functions that perform a task in isolation.
class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self): #instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"discounted price = {final_price}")

l1 = Laptop("16gb", "512gb")

l1.calc_discount(40_000, 10)