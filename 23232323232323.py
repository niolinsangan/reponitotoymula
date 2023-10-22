class Customer:
    def __init__(self, customer_id, name, email, password):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password

    def welcoming(self):
        print(f"Welcome back, {self.name}!")

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, customer,cart):
        self.order_id = order_id
        self.customer = customer
        self.cart = cart
        #hello world

    def place_order(self)
        print(f"Order placed by{self.customer.name} with order ID {self.order_id}.")
        print(f"{item['quantity']} x {item['product'].name}")

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
       
        item = {"product": product, "quantity": quantity}
        self.items.append(item)
        print(f"{quantity} {product.name}(s) added to the cart.")

    def remove_from_cart(self, product):
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)
                print(f"{product.name} removed from the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total += product.price * quantity
        return total