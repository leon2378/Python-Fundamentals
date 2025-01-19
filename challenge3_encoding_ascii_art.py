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
    """
    Decodes a Run-Length Encoded (RLE) list back into the original string.

    Parameters:
        encodedList (List[Tuple[str, int]]): The RLE encoded list.

    Returns:
        str: The original ASCII art string.
    """

    if not encodedList:
        return ""
    
    decoded = []

    for char, count in encodedList:
        decoded.append(char * count)

    return ''.join(decoded)



# Second Method

def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr