# Globalna zmienna przechowującą całkowite saldo banku
saldo_banku = 0

def konto_bankowe(saldo_startowe):
    """Tworzy nowe konto bankowe z początkowym saldem."""
    saldo = saldo_startowe # Zmienna lokalna przechowująca saldo konta

    def wplata(kwota):
        """Dodaje pieniądze do konta i aktualizuje saldo banku."""
        nonlocal saldo
        global saldo_banku
        saldo += kwota
        saldo_banku += kwota
        print(f"Wpłacono {kwota} zł. Nowe saldo konta: {saldo} zł")

    def wyplata(kwota):
        """Odejmuje pieniądze z konta, jeśli saldo na to pozwala."""
        nonlocal saldo
        if saldo >= kwota:
            saldo -= kwota
            global saldo_banku
            saldo_banku -= kwota
            print(f"Wypłacono {kwota} zł. Nowe saldo konta: {saldo} zł")
        else:
            print("Odmowa. Niewystarczające środki!")

    def sprawdz_saldo():
        """Wyświetla saldo konta"""
        print(f"Aktualne saldo: {saldo} zł")

    return {"wplata": wplata, "wyplata": wyplata, "sprawdz_saldo": sprawdz_saldo}


# Testujemy program
konto1 = konto_bankowe(100)
konto1["wplata"](20)
konto1["wyplata"](50)
konto1["sprawdz_saldo"]()