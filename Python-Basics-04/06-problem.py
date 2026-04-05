# "Product store" 
# Design and create an online stire for product(name, price)
# track total products being created.
# create a static method to calculate discount on each product based on a % paramenter
class Product:
    count = 0

    def __init__(self, name, price):
        self.name =name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Price of {self.name} is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products created: {cls.count}")
    
    @staticmethod
    def calc_discount(price, discount):
        print(f"Price after {discount}% discount is: {price - (price * discount / 100)}")

p1=Product("Laptop", 1000)
p2=Product("Phone", 500)
p3=Product("Tablet", 300)

# p1.get_info()
# p2.get_info()

Product.get_count()
p1.calc_discount(p1.price, 10)