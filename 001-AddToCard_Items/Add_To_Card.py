class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            print(f"Not enough stock for {self.name}")

    def increase_stock(self, quantity):
        self.stock += quantity


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.items = []  # list of CartItem objects

    def add_product(self, product, quantity):
        # Check stock availability
        if quantity > product.stock:
            print(f"Sorry, only {product.stock} units of {product.name} available.")
            return

        # Check if product already in cart
        for item in self.items:
            if item.product == product:
                # Update quantity and stock
                if quantity + item.quantity > product.stock:
                    print(f"Sorry, only {product.stock} units of {product.name} available in total.")
                    return
                item.quantity += quantity
                product.reduce_stock(quantity)
                print(f"Added {quantity} more of {product.name} to the cart.")
                return

        # If not in cart, add new CartItem
        self.items.append(CartItem(product, quantity))
        product.reduce_stock(quantity)
        print(f"Added {quantity} of {product.name} to the cart.")

    def remove_product(self, product, quantity):
        for item in self.items:
            if item.product == product:
                if quantity >= item.quantity:
                    # Remove completely
                    product.increase_stock(item.quantity)
                    self.items.remove(item)
                    print(f"Removed all {product.name} from the cart.")
                else:
                    item.quantity -= quantity
                    product.increase_stock(quantity)
                    print(f"Removed {quantity} of {product.name} from the cart.")
                return
        print(f"{product.name} not found in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
        return total

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("Your Cart:")
        for item in self.items:
            print(f"{item.product.name} - Quantity: {item.quantity} - Price per unit: ${item.product.price}")
        print(f"Total Price: ${self.calculate_total():.2f}")

# create products
p1 = Product("Laptop", 1200, 5)
p2 = Product("Mouse", 25, 10)

# create cart
my_cart = Cart()

# add products
my_cart.add_product(p1, 2)  # add 2 laptops
my_cart.add_product(p2, 3)  # add 3 mice

my_cart.show_cart()

# remove products
my_cart.remove_product(p2, 1)  # remove 1 mouse

my_cart.show_cart()
