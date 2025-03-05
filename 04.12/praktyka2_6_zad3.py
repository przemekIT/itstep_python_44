start = int(input("Podaj dolny zakres: "))
end = int(input("Podaj górny zakres: "))

a = min(start, end)
b = max(start, end)

while True:
    number = int(input("Podaj liczbę do sprawdzenia: "))

    if a <= number <= b:
        break
    else:
        print("Liczba poza zakresem, spróbuj ponownie.")

for i in range(a, b + 1):
    if i == number:
        print(f"!{i}!", end = ' ')
    else:
        print(i, end = ' ')




