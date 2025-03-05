import random

liczba_do_odgadnieca = random.randint(1, 100)
print(f"Zgadnij liczbę z zakresu od 1 do 100. Wpisz 0, aby zakończyć grę.")

proby = 0

while True:
    wpis = input("Podaj liczbę: ")
    new_wpis = wpis.strip()

    # Sprawdź, czy użytkownik chce zakończyć
    if new_wpis == "0":
        print("Gra przerwana. Dzięki za grę!")
        break

    # Walidacja wejścia
    if not new_wpis.isdigit():
        print("To nie jest poprawna liczba")
        continue

    # Konwersja na liczbę
    liczba = int(new_wpis)
    proby += 1

    # Sprawdzenie zgadywania
    if liczba < liczba_do_odgadnieca:
        print("Za mało, spróbuj ponownie")
    elif liczba > liczba_do_odgadnieca:
        print("Za dużo, spróbuj ponownie")
    else:
        print(f"Gratulacje! Zgadłeś liczbę {liczba_do_odgadnieca} w {proby} próbach.")

