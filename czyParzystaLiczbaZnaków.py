# # Zadanie 6.2
# # Hasła
# # Informatyk z firmy „KompOK” zapisał w pliku hasla.txt 200 haseł. Każde hasło umieszczone jest w osobnym wierszu pliku.
# Hasło składa się tylko z małych liter alfabetu angielskiego, zaś jego długość wynosi od 3 do 10 znaków.
# Wykorzystując dane zawarte w tym pliku, wykonaj poniższe polecenia. Odpowiedzi do poszczególnych podpunktów zapisz w plikach tekstowych
# o nazwach wynik4a.txt, wynik4b.txt, wynik4c.txt

# a) W pliku wynik4a.txt podaj, ile haseł ma parzystą, a ile nieparzystą liczbę znaków

def czyParzystaLiczbaZnakow(znaki):
    if len(znaki) % 2 == 0:
        return True
    return False


readFile = open("./pliki6/hasla.txt", "r")
writeFile = open("./pliki6/wynik4a.txt", "w")

parzyste = 0
nieparzyste = 0
for line in readFile:
    if czyParzystaLiczbaZnakow(line.replace("\n", "")):
        parzyste += 1
    else:
        nieparzyste += 1

writeFile.write("Parzyste: "+str(parzyste)+"\nNieparzyste: "+str(nieparzyste))
