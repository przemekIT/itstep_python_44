licznik_parzystych = 0

while True:
    liczba = int(input("Podaj liczbę całkowitą (ujemna kończy program): "))
    
    # Sprawdź, czy liczba jest ujemna
    if liczba < 0:
        print("Koniec programu!")
        break

    # Sprawdź, czy liczba jest parzysta
    if liczba % 2 != 0:
        # Jeśli nieparzysta, pomiń resztę kodu
        continue

    licznik_parzystych += 1

print(f"Podałeś {licznik_parzystych} parzystych liczb")

