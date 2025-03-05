print("Prosty kalkulator. Wpisz 'exit', aby zakończyć")

while True:
    # Pobranie operacji od użytkownika
    user_input = input("Podaj operacje (np. 5 + 3) lub 'exit': ").strip().lower()

    if user_input == "exit":
        print("Kalkulator zakończył działanie. Do widzenia!")
        break

    print("Przed wyswietleniem wyniku")
    result = eval(user_input)
    print(f"Wynik: {result}")


print("Po break tutaj przechodzi python")
    


    