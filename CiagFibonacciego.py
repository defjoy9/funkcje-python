# Zadanie 4.12
# Napisz funkcję, która obliczy n-ty wyraz ciągu Fibonacciego (https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego), przy pomocy rekurencji.

def CiagFibonacciego(WyrazCiagu):
    if WyrazCiagu == 0:
        return 0
    elif WyrazCiagu == 1:
        return 1
    elif WyrazCiagu > 1:
        return CiagFibonacciego(WyrazCiagu-1)+CiagFibonacciego(WyrazCiagu-2)


print(CiagFibonacciego(12))
