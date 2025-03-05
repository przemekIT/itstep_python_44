while True :
    dane = input("wprowadz liste liczb odzeil je spacjami potem uzyj ENTER by uruchomić program ")

    if not dane : # Pusta linia kończy program
        print("Zakończono wprowadzanie danych")
        exit()

    try:
        lista = list(map(int, dane.split()))
    # konwersja liczb na liczby całkowiete
        break
    except ValueError:
        print("Błąd: Wprowadź tylko liczby całkowiete, oddzielone spacjami.")

najwieksza = max(lista)
najmnijesza = min(lista)
suma = sum(lista)
srednia = suma / len(lista)
dodatnie = len([x for x in lista if x > 0])
ujemne = len([x for x in lista if x < 0 ])
rowneych_zero = len([x for x in lista if x == 0 ])
wieksze_niz_srednia = [x for x in lista if x > srednia]

# wyświetl statystyke
print(f"najwieksza:", najwieksza)
print(f"najmniejsza", najmnijesza)
print(f"suma ", suma)
print(f"średnia", srednia)
print(f"liczba ujemnych ", ujemne)
print(f"liczba dodatnich ", dodatnie)
print(f"liczy równych zero", rowneych_zero)
print(f"liczby większe niż średnia ", wieksze_niz_srednia)
nowa_lista = [x // 2 if x % 2 == 0 else x * 2 for x in lista]
print(f"nowa lista", nowa_lista)

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
print(f" lista posortowana rosnąco :",{lista})


