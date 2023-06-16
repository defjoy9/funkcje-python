#szyfr 13.1 Cezara

def szyfrowanie(tekst, klucz):
    szyfrogram=""
    klucz = klucz % 26
    for index in range(len(tekst)):
        sumaLiteraPlusKlucz = ord(tekst[index]) + klucz
        if sumaLiteraPlusKlucz > 90:
            szyfrogram = szyfrogram+ chr(sumaLiteraPlusKlucz - 26)
        else: 
            szyfrogram = szyfrogram+ chr(sumaLiteraPlusKlucz)
    return szyfrogram
def ODszyfrowanie(tekst, klucz):
    szyfrogram=""
    klucz = klucz % 26
    for index in range(len(tekst)):
        sumaLiteraPlusKlucz = ord(tekst[index]) - klucz
        if sumaLiteraPlusKlucz < 65:
            szyfrogram = szyfrogram+ chr(sumaLiteraPlusKlucz + 26)
        else: 
            szyfrogram = szyfrogram+ chr(sumaLiteraPlusKlucz)
    return szyfrogram


#TDD :
print(ODszyfrowanie("PDPD",3))

