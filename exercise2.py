# Look at the class diagram below, which represents 
# an association where an Order has a list of Products.

# ---------------------------                   -----------------
# | Order                   |                   | Product       |
# ---------------------------                   -----------------
# | products: List<Product> |------------------ | name: str     |
# ---------------------------               0..*| price: float  |
# | add_product(product)    |                   | quantity: int |
# | calculate_value()       |                   -----------------
# ---------------------------

# add_product(product): takes a Product object and adds it to the product list.
# calculate_value(): must return the total value of the order 
# (sum of product prices multiplied by the number of items)

# Implement the Product and Order classes.


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Order:
    def __init__(self):
        self.products = []


    def add_product(self, product):
        products = self.products.append(product)
        return products


    def calculate_value(self):
        sum = 0
        for product in self.products:
            sum += product.price * product.quantity
        return sum


coffee = Product('Coffee', 5.50, 1)
rice = Product('Rice', 4.90, 2)
bean = Product('Black Bean', 2.80, 2)
my_order = Order()
my_order.add_product(coffee)
my_order.add_product(rice)
my_order.add_product(bean)
print('The total value is $: ', my_order.calculate_value())
   