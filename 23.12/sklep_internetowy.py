koszyk = []
print("Wprowadź produkt i cenę (format: nazwa, cena). Aby zakończyć, naciśnij Enter: ")

while True:
    dane = input()

    if not dane: # Zakończenie wprowadzania
        break

    # Sprawdzenie, czy dane są poprawne
    if "," in dane:
        nazwa, cena = dane.split(",", 1) # Podział na nazwę i cenę
        if cena.strip().isdigit(): # Cena musi być liczbą całkowitą
            koszyk.append((nazwa.strip(), float(cena.strip())))
        else:
            print("Błąd! Wprowadź dane w formacie nazwa, cena.")

# Obliczenia
wartosc_koszyka = sum(cena for _, cena in koszyk)
produkty_drogie = [nazwa for nazwa, cena in koszyk if cena > 50]
srednia_cena = wartosc_koszyka / len(koszyk) if koszyk else 0

print(f"\nCałkowita wartość koszyka: {wartosc_koszyka:.2f} zł")
print(f"Średnia cena produktów: {srednia_cena:.2f} zł")
print(f"Produkty droższe niż 50zł: {produkty_drogie}")

# Zniżki
if wartosc_koszyka > 300:
    koszyk = [(nazwa, cena * 0.9) for nazwa, cena in koszyk]
    wartosc_koszyka = sum(cena for _, cena in koszyk)

koszt_dostawy = 0 if wartosc_koszyka > 250 else 20

if koszt_dostawy > 0:
    koszyk.append(["Dostawa", koszt_dostawy])
wartosc_koszyka += koszt_dostawy


print("\n Nowy koszyk (po zniżkach i dodaniu dostawy)")
for nazwa, cena in koszyk:
    print(f"- {nazwa}: {cena:.2f} zł")

print(f"\n Nowa wartość koszyka: {wartosc_koszyka:.2f} zł")



