def convertCharacterToDigit(character):
    
        if ord(character) >=65:
            return ord(character)- 55
        else:
            return int(character)