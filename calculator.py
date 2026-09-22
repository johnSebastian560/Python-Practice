def calculator():
    first = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    second = float(input("Enter second number: "))

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("Cannot divide by zero.")
            return
        result = first / second
    else:
        print("Invalid operator.")
        return

    print("Result:", result)


if __name__ == "__main__":
    calculator()
