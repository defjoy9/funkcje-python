def convertAnyToDec(napis,system):
    from convertCharacterToDigit import converCharacterToDigit
    dec = 0
    for i in range (len(napis)):
        power = len(napis) - 1 - i
        dec = dec + converCharacterToDigit(napis[i]) * (system ** power)
    return dec
    
print(convertAnyToDec("2A",16))