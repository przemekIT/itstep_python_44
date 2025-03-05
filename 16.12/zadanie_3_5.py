# Pobierz ciąg znaków od użytkownika
ciag_znakow = input("Wpisz ciag znakow: ")
slowo_zastepujace = input("Słowo zastępujące: ")
slowo = input("Podaj slowo, ktore chcesz zamienic: ")
zamieniony_ciag = ciag_znakow.replace(slowo, slowo_zastepujace)

print(f"Nowy zamieniony ciag to: {zamieniony_ciag}")
