



def createDictionary(text):
    """
    create a dictionary of the count of each symbol in given text
    input: str(either ciphertext or plaintext)
    output: dict(each symbol matched to frequency)
    """
    
    frequencies = {}
    
    #create dictionary of space and a-z
    frequencies[chr(32)] = 0
    for asciinumber in range(97,123):
        frequencies[chr(asciinumber)] = 0
    
    #count each letter
    for letter in text:
        frequencies[letter] += 1

    return frequencies


testText = 'wqehrjnjn qwefjknqefbnbhi qjefbn jk jqwebf jinqefj qjeqwoieruuwerzn asnfgkjqjkqf'
frequencyTable = createDictionary(testText)
print(frequencyTable)