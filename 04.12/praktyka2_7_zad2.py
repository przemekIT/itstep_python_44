# szerokosc = int(input("Podaj szerokość prostokąta: "))
wysokosc = int(input("Podaj wysokość prostokąta: "))

for _ in range(wysokosc):
    for _ in range(wysokosc):
        print('*', end='')
    print()