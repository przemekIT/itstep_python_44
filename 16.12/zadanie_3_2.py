# Pobierz ciąg znaków od użytkownika
ciag_znakow = input("Wpisz ciag znakow: ")

# Policzenie liczby liter i cyfr w ciagu
liczba_liter = 0
liczba_cyfr = 0
for c in ciag_znakow:
    if c.isalpha():
        liczba_liter += 1
    elif c.isdigit():
        liczba_cyfr += 1

print(f"Liczba cyfr: {liczba_cyfr}")
print(f"Liczba liter: {liczba_liter}")

