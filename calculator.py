def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (+/-/*/): ")

if choice in operations:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = operations[choice](num1, num2)
    print("Result:", result)
else:
    print("Invalid input")
