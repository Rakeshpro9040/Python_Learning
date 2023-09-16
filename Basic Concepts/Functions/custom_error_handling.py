# Define a custom exception class
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# This will also work
class CustomError1(Exception):
    pass

# This will also work
class CustomError2(ValueError):
    pass

# Function that raises the custom exception
def divide(a, b):
    if b == 0:
        raise CustomError("Division by zero is not allowed.")
    return a / b

# Main program
try:
    result = divide(10, 0)
except CustomError as e:
    print(f"Custom Error: {e}")
else:
    print(f"Result: {result}")