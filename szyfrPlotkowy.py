
# Szyf płotkowy 

def szyfrowanie(tekst,klucz):
    szyfrogram = ""
    plotek = []
    for i in range(klucz):
        plotek.append([])
    wiersz = 0
    wDol = True
    for indexKlucz in range(klucz):
        for index in range(len(tekst)):
            plotek[indexKlucz].append("")

    for index in range (len(tekst)):
        plotek[wiersz][index] = tekst[index]
        if wDol == True and wiersz != klucz - 1:
            wiersz = wiersz + 1
        elif wDol == True and wiersz == klucz -1:
            wiersz = wiersz - 1
            wDol = False
        elif wDol == False and wiersz != 0:
            wiersz = wiersz - 1
        elif wDol == False and wiersz == 0:
            wiersz = wiersz + 1
            wDol = True

    for indexKlucz in range(klucz):
        for index in range(len(tekst)):
            szyfrogram = szyfrogram + plotek[indexKlucz][index]
    return szyfrogram
    print(plotek)



# odszyfrowanie szyfru plotkowego --------------------------------------------------------------------------------------------------------------------------------

def deszyfrowanie(szyfrogram,klucz):
    tekstJawny = ""
    plotek = []
    for i in range(klucz):
        plotek.append([])
    wDol = True
    for indexKlucz in range(klucz):
        for index in range(len(szyfrogram)):
            plotek[indexKlucz].append("")
    wiersz = 0 
    for index in range (len(szyfrogram)):
        plotek[wiersz][index] = "X"
        if wDol == True and wiersz != klucz - 1:
            wiersz = wiersz + 1
        elif wDol == True and wiersz == klucz -1:
            wiersz = wiersz - 1
            wDol = False
        elif wDol == False and wiersz != 0:
            wiersz = wiersz - 1
        elif wDol == False and wiersz == 0:
            wiersz = wiersz + 1
            wDol = True

    indexSzyfrogramu = 0
    for indexKlucz in range(klucz):
        for index in range(len(szyfrogram)):
            if plotek[indexKlucz][index] == "X":
                plotek[indexKlucz][index] = szyfrogram[indexSzyfrogramu]
                indexSzyfrogramu = indexSzyfrogramu + 1

    wDol = True
    wiersz = 0 
    for index in range (len(szyfrogram)):
        tekstJawny = tekstJawny + plotek[wiersz][index]
        if wDol == True and wiersz != klucz - 1:
            wiersz = wiersz + 1
        elif wDol == True and wiersz == klucz -1:
            wiersz = wiersz - 1
            wDol = False
        elif wDol == False and wiersz != 0:
            wiersz = wiersz - 1
        elif wDol == False and wiersz == 0:
            wiersz = wiersz + 1
            wDol = True
    return tekstJawny


print(deszyfrowanie("WSSYTOZK",3))

