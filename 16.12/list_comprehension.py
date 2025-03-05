# Tworzymy listę kwadratów liczb od 1 do 5
kwadraty = []
for i in range(1,6):
    kwadraty.append(i**2)

kwadraty_list_comprehension = [l**2 for l in range(1,6)]

print(kwadraty_list_comprehension)
print(kwadraty)

# Tworzymy listę liczb parzystych
parzyste = []
for i in range(1, 11):
    if i%2 == 0:
        parzyste.append(i)
    else:
        continue

print(parzyste)

parzyste_list_comprehension = [x for x in range(1,11) if x % 2 == 0 and (x == 6 or x == 8)]
print(parzyste_list_comprehension)

# Zastąp liczby parzyste ich kwadratami, a liczby nieparzyste podziel przez 2
liczby = [1,2,3,4,5,6,7,8,9,10]
wynik = [x**2 if x % 2 == 0 else x/2 for x in liczby]
print(wynik)

# Zamień tekst na wielkie litery, jeśli zaczyna się na samogłoskę, a na małe litery, jeśli zaczyna się na spółgłoskę
slowa = ["apple", "banana", "orange", "grape", "umbrella"]
wynik = [s.upper() if s[0].lower() in "aeiou" else s.lower() for s in slowa]
print(wynik)

# Utwórz listę: "pozytywna", "negatywna" lub "zero" w zależności od wartości liczb
liczby = [-5, 0, 4, -2, 9, -1, 0]
wynik = ["pozytywna" if x > 0 else "negatywna" if x < 0 else "zero" for x in liczby]
print(wynik)

# Zamień liczby na ich odwrotność jeśli są dodatnie, na 0 jeśli są zerem, na ich  moduł jeśli są ujemne.
liczby = [-10, -3, 0, 4, 7, -5] # abs(x) => zwraca moduł danej liczby, 1/x 
wynik = [1/x if x > 0 else abs(x) if x < 0 else 0 for x in liczby]
print(wynik)

# Wypisz liczby podzielne przez 3 że są podzielne przez 3, liczb podzielne przez 2 że są podzielne przez 2 oraz liczby podzielne przez 5
# że są podzielne przez 5
liczby = list(range(1,26)) # [1,2,3,....25]
wynik = []
# wynik = [None, None, "Divisible by 2", "Divisible by 3", "Divisible by 2", "Divisible by 5"..........]

# Stwórz listę unikalnych wartości zagnieżdżonych list z dodatkowym filtrowaniem - jeśli liczba jest parzysta, dodaj ją do listy wynikowej
# bez zmian, jeśli jest nieparzysta, pomnóż ją przez 10 i dodaj wynik do listy.
# lst = [1,2,3,3,3] => {1,2,3} unikalne_elementy = set(lst)
zagniezdzone_listy = [[1,2,3], [2,2,3,4,4], [5,6,7,7]]
wynik = list(set([x if x % 2 == 0 else x *10 for sublist in zagniezdzone_listy for x in set(sublist)]))
print(wynik)


