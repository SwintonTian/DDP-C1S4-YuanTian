def add(num1, num2):
    return num1 + num2
def substract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2

def calculator():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Select an operation:"))

    if choice == 1:
        num1 = int(input("Enter number:"))
        num2 = int(input("Enter number:"))
        print(add(num1, num2))
    elif choice == 2:
        num1 = int(input("Enter number:"))
        num2 = int(input("Enter number:"))
        print(substract(num1, num2))
    elif choice == 3:
        num1 = int(input("Enter number:"))
        num2 = int(input("Enter number:"))
        print(multiply(num1, num2))
    elif choice ==4:
        num1 = int(input("Enter number:"))
        num2 = int(input("Enter number:"))
        print(divide(num1, num2))
    else:
        print("Invalid choice. Please enter a valid option.")
