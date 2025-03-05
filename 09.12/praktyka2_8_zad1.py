liczba = None

while True:
    print("\n === MENU ===")
    print("1. Podaj nową liczbę")
    print("2. Policz ilość cyfr")
    print("3. Policz sumę cyfr")
    print("4. Oblicz średnią cyfr")
    print("5. Policz ilość zer")
    print("6. Wyjście")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        wejscie = input("Podaj liczbę całkowitą: ")
        if wejscie.isdigit():
            liczba = int(wejscie)
            print(f"Liczba {liczba} została zapisana.")
        else:
            print("Błąd. Podaj prawidłową liczbę całkowitą.")
    
    elif wybor == "2":
        if liczba is not None:
            dlugosc = 0
            temp = liczba
            while temp > 0:
                temp //= 10 
                dlugosc += 1
            print(f"Liczba {liczba} ma {dlugosc} cyfr.")
        else:
            print("Błąd. Najpierw wybierz opcję 1 i podaj liczbę całkowitą.")

    elif wybor == "3":
        if liczba is not None:
            suma_cyfr = 0
            temp = liczba
            while temp > 0:
                suma_cyfr += temp % 10 
                temp //= 10 
            print(f"Suma cyfr liczby {liczba} wynosi {suma_cyfr}.")
        else:
            print("Błąd. Najpierw wybierz opcję 1 i podaj liczbę całkowitą.")

    elif wybor == "4":
        if liczba is not None:
            suma_cyfr = 0
            dlugosc = 0
            temp = liczba
            while temp > 0:
                suma_cyfr += temp % 10 
                temp //= 10 
                dlugosc += 1
            srednia = suma_cyfr / dlugosc
            print(f"Średnia cyfr liczby {liczba} wynosi {srednia:.2f}.")
        else:
            print("Błąd. Najpierw wybierz opcję 1 i podaj liczbę całkowitą.")

    elif wybor == "5":
        if liczba is not None:
            ilosc_zer = 0
            temp = liczba
            while temp > 0:
                if temp % 10 == 0:
                    ilosc_zer += 1
                temp //= 10 
            print(f"Liczba {liczba} zawiera {ilosc_zer} zer.")
        else:
            print("Błąd. Najpierw wybierz opcję 1 i podaj liczbę całkowitą.")

    elif wybor == "6":
        print("Koniec programu. Do widzenia!")
        break

    else:
        print("Błąd. Nieprawdiłowa opcja. Wybierz ponownie.")