# Pobierz ciąg znaków od użytkownika
ciag_znakow = input("Wpisz ciag znakow: ")
symbol = input("Wpisz symbol, który będziesz chciał/a wyszukać: ")

liczba_wystapien = ciag_znakow.count(symbol)

print(f"Liczba wystąpien dla tego symbolu: {liczba_wystapien}")