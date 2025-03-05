# Zadanie 7
def czy_szczesliwa(liczba):
    # Zamieniamy liczbę na napis, aby móc łatwo uzyskać dostęp do do jej cyfr
    liczba_str = str(liczba)

    if len(liczba_str) != 6:
        return False
    
    # Obliczamy sumę trzech pierwszych i trzech ostatnich cyfr
    pierwsze_trzy = sum(int(cyfra) for cyfra in liczba_str[:3])
    ostatnie_trzy = sum(int(cyfra) for cyfra in liczba_str[3:])

    # Porównujemy sumy
    return pierwsze_trzy == ostatnie_trzy

print(czy_szczesliwa(123420)) # True
print(czy_szczesliwa(723422)) # False
print(czy_szczesliwa(111111)) # True
print(czy_szczesliwa(123456)) # False
