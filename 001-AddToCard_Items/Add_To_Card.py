# Define Product Class
class Product:
    def __init__(self , name , price , stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self , quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print(f"Not enough stock for {self.name}")
    def increase_stock(self ,quantity):
        self.stock += quantity

# Define Cart Item class
class CardItem:
    def __init__(self , product , quantity):
        self.product = product
        self.quantity = quantity