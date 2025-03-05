# licznik dodatnich liczb
licznik_dodatnich = 0

while True:
    liczba = int(input("Podaj liczbę całkowitą (0 kończy program): "))
    
    # Sprawdź, czy liczba jest równa zero
    if liczba == 0:
        print("Koniec programu!")
        break

    # Sprawdź, czy liczba jest ujemna
    if liczba < 0:
        # Jeśli ujemna, pomiń resztę kodu
        continue

    licznik_dodatnich += 1

print(f"Podałeś {licznik_dodatnich} dodatnich liczb")

