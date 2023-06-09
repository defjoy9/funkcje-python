# Zadanie 4.7
# Napisz funkcję, która jako argument przyjmuje liczbę całkowitą i zwraca ilość cyfr tej liczby.

def IloscCyfr(liczba):
    liczba = str(liczba)
    return len(liczba)


liczba = int(input("Wpisz liczbę: "))
print("Jest ",IloscCyfr(liczba)," cyfr w twojej liczbie")
