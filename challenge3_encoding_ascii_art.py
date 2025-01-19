# Python code​​​​​​‌‌​​‌​​​​​​‌‌‌‌​‌​‌​​​​​‌ below

def encodeString(stringVal):
    """
    Encodes a string using Run-Length Encoding (RLE).

    Parameters:
        stringVal (str): The ASCII art string to encode.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains
                               a character and its consecutive count.
    """

    if not stringVal:
        return []
    
    encoded = []
    prev_char = stringVal[0]
    count = 1

    for char in stringVal[1:]:
        if char == prev_char:
            count+=1
        else:
            encoded.append((prev_char, count))
            prev_char = char
            count = 1

    # Append the last run
    encoded.append((prev_char, count))

    return encoded


def decodeString(encodedList):
    # Your code goes here.
    pass