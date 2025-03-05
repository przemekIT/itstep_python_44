def dodaj_zamowienie(zamowienia, klient, produkt, ilosc, cena):
    zamowienia.setdefault(klient, []).append({"produkt": produkt, "ilosc": ilosc, "cena": cena})
    return f"Dodano zamówienie dla {klient}: {produkt}, {ilosc} szt. po {cena} zł"

def suma_zamowien(zamowienia, klient):
    return sum(z["ilosc"] * z["cena"] for z in zamowienia.get(klient, []))

def usun_zamowienie(zamowienia, klient, indeks):
    if klient not in zamowienia or indeks >= len(zamowienia[klient]):
        return "Nie znaleziono klienta lub zamowienia"
    zamowienie = zamowienia[klient].pop(indeks)
    return f"Usunięto zamówienie: {zamowienie['produkt']}, {zamowienie['ilosc']} szt."

def najlepszy_klient(zamowienia):
    if not zamowienia:
        return "Brak zamówień."
    return max(zamowienia, key=lambda k: suma_zamowien(zamowienia, k))


zamowienia = {}

print(dodaj_zamowienie(zamowienia, "klient_1", "Laptop", 1, 3000))
print(dodaj_zamowienie(zamowienia, "klient_2", "Myszka", 2, 100))
print(dodaj_zamowienie(zamowienia, "klient_1", "Telefon", 1, 2500))
print(dodaj_zamowienie(zamowienia, "klient_2", "Słuchawki", 3, 1000))

print(f"Suma zamówień klient_1: {suma_zamowien(zamowienia, 'klient_1')} zł")
print(f"Suma zamówień klient_2: {suma_zamowien(zamowienia, 'klient_2')} zł")

print(f"Najlepszy klient: {najlepszy_klient(zamowienia)}")
print(f"Suma zamówień klient_1: {suma_zamowien(zamowienia, 'klient_1')} zł")
print(f"Suma zamówień klient_2: {suma_zamowien(zamowienia, 'klient_2')} zł")
