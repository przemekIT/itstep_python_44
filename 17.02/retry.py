import time
import random

def retry(max_entries=3, delay = 1):
    def dekorator(funkcja):
        def wrapper(*args, **kwargs):
            for attempt in range(max_entries): # Iteracja po próbach
                wynik = funkcja(*args, **kwargs) # Wywołanie funkcji
                if wynik: # Jeśli wynik jest poprawny (True), zwracamy go i nie wykonujemy dalszej części kodu
                    return wynik
                print(f"Niepowodzenie ({attempt + 1}). Próba ponowanego wykonania...")
                time.sleep(delay) # Opóźnienie przez kolejną próbą
            print(f"Nie udało się wykonać {funkcja.__name__} po max {max_entries} próbach.")
            return None # Jeśli po wszystkich próbach wynik nadal jest niepoprawny, zwracamy None
        return wrapper # Zwracamy funkcję opakowującą
    return dekorator # Zwracamy dekorator (opakowany przez funkcję retry, za pomocą której dodajemy argumenty do dekoratora)


@retry(max_entries=10, delay = 2)
def losowa_funkcja():
    return random.choice([True, False]) # 50% szans na sukces funkcji


print(losowa_funkcja())