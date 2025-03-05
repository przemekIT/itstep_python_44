import time

def dekorator(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        end = time.time()
        print(f"Funkcja {funkcja.__name__} wykona w {end-start:.6f} sekundy")
        return wynik
    return wrapper

@dekorator
def wykonaj_obliczenia():
    suma = 0
    for i in range(10**6):
        suma += i
    return suma

wynik = wykonaj_obliczenia()
print(f"Wynik obliczeń: {wynik}")



