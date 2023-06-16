# Szyfr Vigenere
def szyfrowanieVigenere(tekst,klucz):
    tablica =[]
    for indexWiersza in range (26):
        tablica.append([])
        indexLitery = 65 + indexWiersza
        for indexKolumna in range(26):
            tablica[indexWiersza].append(chr(indexLitery))
            indexLitery = indexLitery + 1
            if indexLitery > 90:
                indexLitery = 65

    for index in range(len(tekst)):
        literaZKlucza = klucz[index]
        literaZtekstu = tekst[index]

        szukanaKolumna = ord(literaZKlucza) - 65
        szukanyWiersz = ord(literaZtekstu) - 65
    szyfrogram = ''
    szyfrogram = szyfrogram + (tablica[szukanyWiersz][szukanaKolumna])

    return szyfrogram

# ___________________________________________________________________________________________________________________________________


def deszyfrowanieVigenere(szyfrogram,klucz):
    tablica =[]
    tekstJawny = ''
    for indexWiersza in range (26):
        tablica.append([])
        indexLitery = 65 + indexWiersza
        for indexKolumna in range(26):
            tablica[indexWiersza].append(chr(indexLitery))
            indexLitery = indexLitery + 1
            if indexLitery > 90:
                indexLitery = 65
    for indexLiteryZSzyfrogramu in range(len(szyfrogram)):
        literaZKlucza = klucz[indexLiteryZSzyfrogramu]
        indexLiteryZSzyfrogramu = szyfrogram[indexLiteryZSzyfrogramu]
        szukanaKolumna = ord(literaZKlucza) - 65
        szukanyWiersz = 0
        for wiersz in range(26):
            if tablica[wiersz[szukanaKolumna]] == indexLiteryZSzyfrogramu:
                szukanyWiersz = wiersz
        
    literaZTekstuJawnego = chr(szukanyWiersz) + 65
    tekstJawny = tekstJawny + literaZTekstuJawnego

    return tekstJawny

wartoscTekstuJawnego = "INFORMATYKA"
wartoscKlucza = "PROGRAMOWANIE"
szyfrogram = "XETUIMMHUKN"
print(deszyfrowanieVigenere(szyfrogram,wartoscKlucza))

