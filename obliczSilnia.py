# Zadanie 4.10
# Napisz funkcję, która wyznacza wartość n! (n jest liczbą naturalną). Funkcja ma wykorzystywać iterację.

# np. 5! = 1*2*3*4*5=120


def oblicz_silnie(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Nie można obliczyć silni z liczby ujemnej!"
    else:
        silnia = 1
        for i in range(1, n + 1):
            silnia *= i
        return silnia


print(oblicz_silnie(5))
