# Zadanie 4.4
# Napisz funkcję, która sprawdza, czy podany w argumencie wyraz jest palindromem.
# Nie korzystaj z wbudowanych funkcji**
# **Wyjątkiem jest funckja len()

def CzyJestPalindromem(wyraz):
    for index in range(len(wyraz)):
        if wyraz[index] != wyraz[len(wyraz) - index - 1]:
            return False
        return True


slowo = input("Wpisz słowo: ")

print(CzyJestPalindromem(slowo))
