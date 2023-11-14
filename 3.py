
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero!"

if __name__ == "__main__":
    print("Welcome to simple calculator.")
    print("I will add/subtract/multiply/divide any two numbers you provide.")
    first_input = input("Enter the first number: ")
    second_input = input("Enter the second number: ")
    operation = input("Would you like to add/subtract/multiply/divide: ")

    first_number = float(first_input)
    second_number = float(second_input)

    if operation == "add":
        result = add(first_number, second_number)
        print(f"Result: {result}")
    elif operation == "subtract":
        result = subtract(first_number, second_number)
        print(f"Result: {result}")
    elif operation == "multiply":
        result = multiply(first_number, second_number)
        print(f"Result: {result}")
    elif operation == "divide":
        result = divide(first_number, second_number)
        print(f"Result: {result}")
    else:
        print("Sorry, I do not understand your request.")
