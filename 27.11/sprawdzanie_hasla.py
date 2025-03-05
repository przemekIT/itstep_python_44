# ustawienia
prawidlowe_haslo = "tajnehaslo"
proby_pozostale = 3

while proby_pozostale > 0:
    # Pobierz hasło od użytkownika
    haslo = input("Podaj hasło: ")

    # Sprawdź, czy hasło jest poprawne
    if haslo == prawidlowe_haslo:
        print("Hasło poprawne! Dostęp przyznany.")
        break

    # Hasło niepoprawne
    proby_pozostale -= 1
    if proby_pozostale > 0:
        print(f"Niepoprawne hasło. Pozostało prób {proby_pozostale}")
    else:
        print(f"Przekroczono limit prób. Dostęp zablokowany")
