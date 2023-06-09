# Program, czy liczba jest doskonała
def CzyLiczbaJestDoskonala(liczba):
    suma = 0
    for dzielnik in range (1,liczba):
        if liczba % dzielnik == 0:
            suma = suma + dzielnik
    if suma == liczba:
        return True
    else:
        return False
    
print(CzyLiczbaJestDoskonala(6))

