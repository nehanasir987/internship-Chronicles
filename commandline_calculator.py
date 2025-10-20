def calculator():
    print("=== Command Line Calculator ===")
    print("Operators: +  -  *  /  %  | Type 'exit' to quit\n")

    while True:
        num1 = input("Enter first number: ")
        if num1.lower() == 'exit': break
        num2 = input("Enter second number: ")
        if num2.lower() == 'exit': break
        op = input("Enter operator: ")
        if op.lower() == 'exit': break

        try:
            num1 = float(num1)
            num2 = float(num2)
            if op == '+': 
                result = num1 + num2
            elif op == '-': 
                result = num1 - num2
            elif op == '*': 
                result = num1 * num2
            elif op == '/': 
                result = num1 / num2 if num2 != 0 else "Error (divide by zero)"
            elif op == '%': 
                result = num1 % num2
            else:
                print("Invalid operator!\n")
                continue
            print("Result:", result, "\n")
        except ValueError:
            print("Invalid input! Please enter numbers.\n")

    print("Goodbye!")

if __name__ == "__main__":
    calculator()
