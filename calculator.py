def addition(p, q):
    return p + q

def subtract(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p, q):
    if q == 0:
        return "Cannot divide by zero"
    return p / q

def modulo(p,q):
    return p%q

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'modulo' for  Modulo Division")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["add", "subtract", "multiply", "divide","modulo"]:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result:", addition(number1, number2))
        elif user_input == "subtract":
            print("Result:", subtract(number1, number2))
        elif user_input == "multiply":
            print("Result:", multiply(number1, number2))
        elif user_input == "divide":
            print("Result:", divide(number1, number2))
        elif user_input == "modulo":
            print("Result:", modulo(number1, number2))
    else:
        print("Invalid input. Please enter a valid operation.")
