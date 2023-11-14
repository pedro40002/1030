# main.py
import calculator

def get_user_input():
    first_input = input("Enter the first number: ")
    second_input = input("Enter the second number: ")
    operation = input("Would you like to add/subtract/multiply/divide: ")
    return float(first_input), float(second_input), operation

def main():
    first_number, second_number, operation = get_user_input()

    if operation in ["add", "subtract", "multiply", "divide"]:
        result = getattr(calculator, operation)(first_number, second_number)
        print(f"Result: {result}")
    else:
        print("Sorry, I do not understand your request.")

if __name__ == "__main__":
    main()
