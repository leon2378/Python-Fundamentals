import json 

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    # Loop over the string exactly once.
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count += 1
    # Append the final run.
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    # Instead of repeatedly concatenating strings (which is O(n^2) in worst case),
    # we accumulate pieces in a list and join them once.
    pieces = []
    for char, count in encodedList:
        pieces.append(char * count)
    return ''.join(pieces)

def encodeFile(filename, newFilename):
    """
    Reads the contents of the file 'filename', encodes the text using the
    encodeString function, and writes the encoded list to 'newFilename'
    in JSON format.
    """
    # Reading the file is O(n)
    with open(filename, 'r') as infile:
        fileContent = infile.read()
    
    # Encoding the file content is O(n)
    encodedList = encodeString(fileContent)
    
    # Writing the JSON-encoded list is O(n)
    with open(newFilename, 'w') as outfile:
        json.dump(encodedList, outfile)

def decodeFile(filename):
    """
    Reads an encoded file (in JSON format) from 'filename', decodes it using
    the decodeString function, and returns the decoded string.
    """
    # Reading the JSON file is O(n)
    with open(filename, 'r') as infile:
        encodedList = json.load(infile)
    
    # Decoding the string is O(n)
    return decodeString(encodedList)



# Second Method

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

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    with open(filename) as f:
        data = encodeString(f.read())

def decodeFile(filename):
    with open(filename) as f:
        data = f.read()
    return decodeString(json.loads(data))

    
# Third Method
def encodeFile(filename, newFilename):
    with open(filename) as f:
        data = encodeString(f.read())

    data = [f'{char}|{count}' for char, count in data]

    with open(newFilename, 'w') as f:
        f.write('~'.join(data))

def decodeFile(filename):
    with open(filename) as f:
        data = f.read()

    pairs = data.split('~')
    pairs = [p.split('|') for p in pairs]
    pairs = [(p[0], int(p[1])) for p in pairs]
    return decodeString(pairs)


# Fourth Method (Byte solution)

def encodeFile(filename, newFilename):
    with open(filename) as f:
        data = encodeString(f.read())
    output = bytearray()
    for item in data:
        # Character byte
        output.extend(bytes(item[0], 'utf-8'))
        # integer count byte
        output.extend(item[1].to_bytes(1, 'utf-8'))
    with open(newFilename, 'wb') as binary_file:
        # write bytes to file
        binary_file.write(output)

def decodeFile(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        # split data into pairs
        bytePairs = [data[i:i+2] for i in range (0, len(data), 2)]
        encodedList = []
        for bytePair in bytePairs:
            encodedList.append((bytePair[:1].decode('utf-8'), int.from_bytes(bytePair[1:], 'big')))
        return decodeString(encodedList)