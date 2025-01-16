# Python code​​​​​​‌‌​​​‌‌‌‌‌‌​​​‌​​​‌​​‌‌‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    # Initialize the decimal value to 0
    decimal = 0
    # Convert the input to uppercase to handle lowercase letters
    hexNum = hexNum.upper()
    
    for char in hexNum:
        if char in hexNumbers:
            # Multiply the current total by 16 and add the value of the current hex digit
            decimal = decimal * 16 + hexNumbers[char]
        else:
            # If an invalid character is found, return None
            return None
    return decimal

# Example usage:
print(hexToDec("1A3"))    # Output: 419
print(hexToDec("FF"))     # Output: 255
print(hexToDec("G1"))     # Output: None (invalid character 'G')
print(hexToDec("abcd"))   # Output: 43981



# Second Method:

def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
        
    if len(hexNum) == 3:
        return hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]]
    
    if len(hexNum) == 2:
        return hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]]

    if len(hexNum) == 1:
        return hexNumbers[hexNum[0]] 