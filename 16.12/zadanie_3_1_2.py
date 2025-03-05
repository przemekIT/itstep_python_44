import string

tekst = input("Wpisz tekst: ")

# Zmien tekst tak, aby każde zdanie zaczynało się wielką literą
zdania = tekst.split('. ')
tekst_kapitalizowany = '' 
for zdanie in zdania:
    tekst_kapitalizowany += zdanie.capitalize() + '. '
tekst_kapitalizowany = tekst_kapitalizowany.strip()

liczba_liczb = 0
liczba_interpunkcji = 0
liczba_wykrzyknikow = 0
for znak in tekst:
    if znak.isdigit():
        liczba_liczb += 1
    elif znak == "!":
        liczba_interpunkcji += 1
        liczba_wykrzyknikow += 1
    elif znak == "," or znak == ".":
        liczba_interpunkcji += 1



print(f"\n Liczba liczb w tekście: {liczba_liczb}")
print(f"\n Liczba znaków interpunkcyjnych: {liczba_interpunkcji}")
print(f"\n Liczba wykrzykników w tekście: {liczba_wykrzyknikow}")




