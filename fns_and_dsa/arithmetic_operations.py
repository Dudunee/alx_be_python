def perform_operation(num1: float, num2: float, operation: str) -> float:
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            print("cannot devide by zero")
    else:
        print("Invalid operation")
    



