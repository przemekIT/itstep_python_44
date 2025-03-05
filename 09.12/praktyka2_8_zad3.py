import random

print("Wybierz poziom trudności: ")
print("1. Łatwy (liczby 1-5)")
print("2. Średni (liczby 1-10)")
print("3. Trudny (liczby 1-12)")

poziom = int(input("Wybierz poziom (1/2/3): "))

if poziom == 1:
    zakres = 5
    pytania = 2
elif poziom == 2:
    zakres = 10
    pytania = 5
elif poziom == 3:
    zakres = 12
    pytania = 10
else:
    print("Nieprawidłowy wybór poziomu")
    exit()

punkty = 0

for i in range(pytania):
    a = random.randint(1, zakres)
    b = random.randint(1, zakres)

    print(f"Co to jest {a} * {b}?")
    odpowiedz = int(input("Wpisz wynik: "))

    if odpowiedz == a*b:
        print("Dobrze!")
        punkty += 1
    else:
        print(f"Źle! Poprawna odpowiedź to {a * b}.")

print(f"\n Twoje punkty: {punkty} na {pytania} możliwych")