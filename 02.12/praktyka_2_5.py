# Zadanie 1
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))

# # Normalizacja zakresu
# start = min(a,b)
# end = max(a,b)
# suma = 0

# # Obliczanie sumy i średniej
# for i in range(start, end + 1):
#     suma += i

# liczba_elementow = end - start + 1
# srednia = suma / liczba_elementow

# print(f"Suma liczb w zakresie od {start} do {end}: {suma}")
# print(f"Średnia liczb w zakresie od {start} do {end}: {srednia:.2f}")

# # Zadanie 2
# n = int(input("Podaj liczbę: "))

# if n<0:
#     print("Silnia jest zdefiniowana tylko dla liczb nieujemnych")

# silnia = 1

# for i in range(1, n+1):
#     silnia *= i

# print(f"Silnia z liczby {n} wynosi: {silnia}")


# Zadanie 3
# dlugosc = int(input("Podaj długość linii: "))
# # linia = ''

# if dlugosc <= 0:
#     print("Długość lini musi być większa od zera")
# else:
#     for i in range(dlugosc):
#         print('*', end = '')
#     # print(linia)

# Zadanie 4
dlugosc = int(input("Podaj długość linii: "))
znak = input('Podaj znak: ')
# linia = ''

if dlugosc <= 0:
    print("Długość lini musi być większa od zera")
else:
    for i in range(dlugosc):
        print(znak, end = '')
    # print(linia)