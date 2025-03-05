import random
import time
print(time.time()) 

liczba_do_odgadniecia = random.randint(1,500) # <1,500>, range(1,500) => <1,500)
print("Witaj w grze 'Zgadnij liczbę'!")
print("Wpisz 0, aby zakończyć grę.")

proby = 0 # Liczba prób
start_czasu = time.time() # Start pomiaru czasu

while True:
    odpowiedz = int(input("Podaj liczbę: "))

    # Sprawdź, czy użytkownik chce zakończyć grę
    if odpowiedz == 0:
        print("Gra zakończona. Dziękujemy za udział!")
        break

    proby += 1

    if odpowiedz < liczba_do_odgadniecia:
        print("Za mało, spróbuj ponownie większej liczby!")
    elif odpowiedz > liczba_do_odgadniecia:
        print("Za dużo, spróbuj ponownie mniejszej liczby!")
    else:
        # Użytkownik odgadł liczbę
        czas_trwania = time.time() - start_czasu
        print(f"Brawo! Odgadłeś liczbę {liczba_do_odgadniecia}.")
        print(f"Liczba prob: {proby}")
        print(f"Czas gry: {czas_trwania} sekund.")
        break


print(time.time() - start_czasu2)

