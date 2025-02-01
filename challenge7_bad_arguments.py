# Define the custom exception
class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        # Check each argument in *args
        for arg in args:
            if not isinstance(arg, int):
                raise NonIntArgumentException(f"Argument {arg} is not an integer.")
        # All arguments are integers; call the function and return its result.
        return func(*args)
    return wrapper

# Example usage with a function that sums its arguments.
@handleNonIntArguments
def my_sum(*args):
    return sum(args)


# Second Method

class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        for item in args:
            if type(item) is not int:
                raise NonIntArgumentException()
        return func(*args)
    return wrapper