import time

def mierzenie_czasu(jednostka="s"):
    def dekorator(funkcja):
        def wrapper(*args, **kwargs):
            start = time.time()
            wynik = funkcja(*args, **kwargs)
            end = time.time()
            czas_trwania = end - start

            if jednostka == "ms":
                czas_trwania *= 1000
            
            print(f"Funkcja {funkcja.__name__} wykona w {czas_trwania:.6f} {jednostka}")
            return wynik
        
        return wrapper
    return dekorator


@mierzenie_czasu(jednostka = "s")
def zadanie():
    time.sleep(2)

@mierzenie_czasu(jednostka = "ms")
def szybkie_zadanie():
    time.sleep(0.1)

zadanie()
szybkie_zadanie()
