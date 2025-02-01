def handleNonIntArguments(func):
    def wrapper(*args, **kwargs):
        # Process positional arguments in O(n) time
        new_args = []
        for arg in args:
            if not isinstance(arg, int):
                try:
                    arg = int(arg)
                except Exception as e:
                    raise TypeError(f"Argument {arg} cannot be converted to int.") from e
            new_args.append(arg)
        
        # Process keyword arguments in O(n) time
        new_kwargs = {}
        for key, value in kwargs.items():
            if not isinstance(value, int):
                try:
                    value = int(value)
                except Exception as e:
                    raise TypeError(f"Keyword argument {key}={value} cannot be converted to int.") from e
            new_kwargs[key] = value
        
        return func(*new_args, **new_kwargs)
    return wrapper

# Example usage:

@handleNonIntArguments
def add(a, b):
    return a + b

@handleNonIntArguments
def multiply(a, b):
    result = 0
    # Multiply by repeated addition (without using the * operator)
    for _ in range(b):
        result += a
    return result

# Test the decorator:
print(add(3, 4))            # Expected output: 7
print(add("10", "20"))      # Expected output: 30 (arguments converted to integers)
print(multiply(5, "3"))     # Expected output: 15 (5 added 3 times)
