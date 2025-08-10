# Define Product Class
class Product:
    def __init__(self , name , price , stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self , quantity):
        if quantity <= self.stock:
            self.stock -= quantity
    def increase_stock(self ,quantity):
        self.stock += quantity