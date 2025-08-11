# # Simple Calculator in Python

# # Function for addition
# def add(x, y):
#     return x + y

# # Function for subtraction
# def subtract(x, y):
#     return x - y

# # Function for multiplication
# def multiply(x, y):
#     return x * y

# # Function for division
# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y

# # Menu
# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
#     print(f"Result: {add(num1, num2)}")
# elif choice == '2':
#     print(f"Result: {subtract(num1, num2)}")
# elif choice == '3':
#     print(f"Result: {multiply(num1, num2)}")
# elif choice == '4':
#     print(f"Result: {divide(num1, num2)}")
# else:
#     print("Invalid input")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select one option")
print("1: for Add")
print("2: for Subtract")
print("3: for Multiply")
print("4: for Divide")

choice = input("Choose an option from above: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print(f"Result: {add(num1, num2)}")
elif choice == "2":
    print(f"Result: {subtract(num1, num2)}")
elif choice == "3":
    print(f"Result: {multiply(num1, num2)}")
elif choice == "4":
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid input")
    