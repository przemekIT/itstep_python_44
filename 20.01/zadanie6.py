from datetime import datetime

# Funkcja sprawdzająca, czy rok jest przestępny
def czy_rok_przestępny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
        return True
    return False

def roznica_dni(dzien1, miesiac1, rok1, dzien2, miesiac2, rok2):
    # Tworzymy obie daty
    data1 = datetime(rok1, miesiac1, dzien1)
    data2 = datetime(rok2, miesiac2, dzien2)
    
    # Obliczamy różnicę dni
    roznica = data2 - data1
    return abs(roznica.days)

print(roznica_dni(9,5,2006, 10, 6, 2006))
