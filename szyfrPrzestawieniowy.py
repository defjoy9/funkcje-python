# szyfr przestawieniowy


def szyfrowanie(tekst):
    szyfrogram = ""
    for index in range (0,len(tekst)-1,2):
        szyfrogram = szyfrogram + tekst[index + 1]
        szyfrogram = szyfrogram + tekst[index]
    if len(tekst) % 2 == 1:
        szyfrogram = szyfrogram + tekst[len(tekst)-1]
    return szyfrogram 


print(szyfrowanie("INFORMATYKA"))


# TO-DO : odszyfrowanie
