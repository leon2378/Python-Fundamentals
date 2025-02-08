# # Python code​​​​​​‌‌​​‌​‌​​​‌‌‌‌​​‌​‌​‌‌​‌‌ below
# import json 

# def encodeString(stringVal):
#     encodedList = []
#     prevChar = None
#     count = 0
#     for char in stringVal:
#         if prevChar != char and prevChar is not None:
#             encodedList.append((prevChar, count))
#             count = 0
#         prevChar = char
#         count = count + 1
#     encodedList.append((prevChar, count))
#     return encodedList

# def decodeString(encodedList):
#     decodedStr = ''
#     for item in encodedList:
#         decodedStr = decodedStr + item[0] * item[1]
#     return decodedStr

# # The filename that will be passed to this function
# # is 10_04_challenge_art.txt
# def encodeFile(filename, newFilename):
#     # Your code goes here.
#     pass

# def decodeFile(filename):
#     # Your code also goes here.
#     pass
    


import json 

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
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

def encodeFile(filename, newFilename):
    """
    Reads the contents of the file 'filename', encodes the text using the
    encodeString function, and writes the encoded list to 'newFilename'
    in JSON format.
    """
    # Read the original file
    with open(filename, 'r') as infile:
        fileContent = infile.read()
    
    # Encode the file content
    encodedList = encodeString(fileContent)
    
    # Write the encoded list to newFilename in JSON format
    with open(newFilename, 'w') as outfile:
        json.dump(encodedList, outfile)

def decodeFile(filename):
    """
    Reads an encoded file (in JSON format) from 'filename', decodes it using
    the decodeString function, and returns the decoded string.
    """
    # Read the encoded data from file
    with open(filename, 'r') as infile:
        encodedList = json.load(infile)
    
    # Decode the encoded list and return the decoded string
    return decodeString(encodedList)

# Example usage:
if __name__ == "__main__":
    # Suppose "10_04_challenge_art.txt" contains some ASCII art.
    # We'll encode it and save the encoded version as "encoded_art.json"
    encodeFile("10_04_challenge_art.txt", "encoded_art.json")
    
    # Now, decode the file and print the original art
    original_art = decodeFile("encoded_art.json")
    print(original_art)
