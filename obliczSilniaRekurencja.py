# Zadanie 4.11
# Napisz funkcję, która wyznacza wartość n! (n jest liczbą naturalną). Funkcja ma wykorzystywać rekurencję.


def oblicz_silnie(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Nie można obliczyć silni z liczby ujemnej!"
    else:
        return n * oblicz_silnie(n - 1)


print(oblicz_silnie(5))
