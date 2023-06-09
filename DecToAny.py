def convertDecToAny(liczba,system):
    wynik =""
    while liczba>0:
        if liczba % system >=10:
            #używamy słownika
            litery = {
                "10":"A",
                "11":"B",
                "12":"C",
                "13":"D",
                "14":"E",
                "15":"F"
            }
            wynik = litery[str(liczba % system)]+wynik 
            #bez słownika ASCII
            # 65 = A = char(55 + liczba % system) 
        else:
            wynik =str(liczba % system)+wynik 

        liczba = int(liczba /system)
    return wynik

liczba = int(input("Podaj liczbe w 10: "))
system = int(input("Na jaki system: "))


print(convertDecToAny(liczba,system))