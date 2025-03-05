while True:
    # Pobieranie liczby sekund od użytkownika
    wartosc = input("Podaj czas w sekundach od początku dnia: ")
    if wartosc.isdigit():
        sekundy_od_poczatku_dnia = int(wartosc)
        if sekundy_od_poczatku_dnia < 0 or sekundy_od_poczatku_dnia >= 24 * 3600:
            print("Podana liczba sekund musi być z zakresu od 0 do 86399.")
            continue
        else:
            # Całkowita liczba sekund w jednym dniu
            sekundy_w_dniu = 24 * 3600

            # Obliczanie pozostałego czasu do północy:
            sekundy_do_polnocy = sekundy_w_dniu - sekundy_od_poczatku_dnia
            godziny = sekundy_do_polnocy // 3600
            minuty = (sekundy_do_polnocy % 3600) // 60
            sekundy = sekundy_do_polnocy % 60

            # Wyswietlanie wyniku
            print(f"Do północy pozostało: {godziny} godzin, {minuty} minut i {sekundy} sekund.")
            break
    else:
        print("Podana wartość nie jest poprawną liczbą całkowitą")
        continue

# break - automatycznie wychodzi i kończy pętle
# continue - przechodzi do następnej iteracji

