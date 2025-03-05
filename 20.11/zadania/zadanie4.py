# Pobieranie danych od użytkownika 
rozmiar_gb = float(input("Podaj rozmiar pliku w gigabajtach (GB): "))
przepustowosc_bps = float(input("Podaj przepustowość łącza w bitach na sekunde: "))

# Przeliczanie roamiaru pliku na bity
rozmiar_bit = rozmiar_gb * 8 * (1024**3)

# Obliczanie czasu pobierania w sekundach
czas_w_sekundach = rozmiar_bit / przepustowosc_bps

print("\nWybierz jednostkę czasu:")
print("1 - godziny")
print("2 - minuty")
print("3 - sekundy")

wybor = input("Twój wybór 1/2/3: ")

if wybor == "1":
    czas_godziny = czas_w_sekundach / 3600
    print(f"Czas pobierania: {czas_godziny:.2f} godzin")
elif wybor == "2":
    czas_minuty = czas_w_sekundach / 60
    print(f"Czas pobierania: {czas_minuty:.2f} minut")
elif wybor == "3":
    print(f"Czas pobierania: {czas_w_sekundach:.2f} sekund")
else:
    print("Nieprawidłowy wybór. Spróbuj ponownie.")
