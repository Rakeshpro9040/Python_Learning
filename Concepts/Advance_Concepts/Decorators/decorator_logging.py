import functools
import datetime

# Define the log_to_file decorator
def log_to_file(file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] Calling function: {func.__name__}\n"

            with open(file_path, "a") as log_file:
                log_file.write(log_message)

            result = func(*args, **kwargs)

            log_message = f"[{timestamp}] {func.__name__} returned: {result}\n"

            with open(file_path, "a") as log_file:
                log_file.write(log_message)

            return result
        return wrapper
    return decorator

# Apply the decorator to multiple functions and specify the log file path
@log_to_file("./Advance Concepts/Decorators/function_log.log")
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

@log_to_file("./Advance Concepts/Decorators//function_log.log")
def multiply(x, y):
    return x * y

@log_to_file("./Advance Concepts/Decorators//function_log.log")
def subtract(p, q):
    return p - q

# Call the decorated functions
result1 = divide(10, 2)
result2 = multiply(5, 3)
result3 = subtract(8, 4)
