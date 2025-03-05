# Globalna zmienna do przechowywania sumy wszystkich punktów
punkty_globalne = 0

def gra(punkty_startowe):
    """Symuluje rozgrywkę, gdzie gracz zdobywa pinkty i może otrzymać bonus."""
    punkty_lokalne = punkty_startowe # Punkty zdobyte w danej grze

    def bonus():
        """Dodaje bonusowe punkty do wyniku tej gry."""
        nonlocal punkty_lokalne # Odwołanie do zmiennej z ecnlosing scope
        punkty_lokalne += 5 # Dodajemy bonus

    bonus() # Przyznanie

    global punkty_globalne # Odwołanie do globalnej sumy punktów
    punkty_globalne += punkty_lokalne

    print(f"Gracz zdobył {punkty_lokalne} punktów (z bonusem 5).")

gra(10)
gra(20)
print("Suma wszystkich punktów: ", punkty_globalne)