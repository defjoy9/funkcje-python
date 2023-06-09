# Zadanie 4.8
# Napisz funkcję, która jako argument przyjmuje liczbę. Funkcja ma sprawdzić, czy podana liczba jest pierwsza.

def CzyPierwsza(liczba):
    if liczba == 2:
        return True
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


cyfra = int(input("Wpisz cyfrę: "))
print(CzyPierwsza(cyfra))
