# Zadanie 2
while True:
    # kursy względem 1 zł
    kurs_usd = 0.23
    kurs_eur = 0.22
    kurs_pln = 1.0
    kurs_gbp = 0.19
    kurs_jpy = 33.72

    print("Dostępne waluty: USD, EUR, PLN, GBP, JPY")

    # Pobranie waluty wejściowej
    if not wejscie:
        wejscie = input("W jakiej walucie chcesz wpisać kwotę? (USD, EUR, PLN, GBP, JPY): ")
        if wejscie == "USD":
            kurs_wejscie = kurs_usd
        elif wejscie == "EUR":
            kurs_wejscie = kurs_eur
        elif wejscie == "PLN":
            kurs_wejscie = kurs_pln
        elif wejscie == "GBP":
            kurs_wejscie = kurs_gbp
        elif wejscie == "JPY":
            kurs_wejscie = kurs_jpy
        else:
            print("Nieprawidłowa waluta wejściowa! Wpisz ponownie")
            continue

    
    # Pobranie waluty docelowej
    if not wyjscie:
        wyjscie = input("Na jaką walutę chcesz przeliczyć? (USD, EUR, PLN, GBP, JPY): ")
        if wyjscie == "USD":
            kurs_wyjscie = kurs_usd
        elif wyjscie == "EUR":
            kurs_wyjscie = kurs_eur
        elif wyjscie == "PLN":
            kurs_wyjscie = kurs_pln
        elif wyjscie == "GBP":
            kurs_wyjscie = kurs_gbp
        elif wyjscie == "JPY":
            kurs_wyjscie = kurs_jpy
        else:
            print("Nieprawidłowa waluta docelowa! Wpisz ponownie")
            continue    

    kwota = input(f"Podaj kwotę w {wejscie}: ")

    if kwota.isdigit():
        kwota_float = float(kwota)
    else:
        print("Wpisz poprawną kwotę")
        continue

    # Przeliczenie waluty
    kwota_w_pln = kwota_float / kurs_wejscie
    wynik = kwota_w_pln * kurs_wyjscie

    print(f"{kwota_float:.2f} {wejscie} = {wynik:.2f} {wyjscie}")

    break

