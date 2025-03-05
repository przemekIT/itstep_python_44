temperatura = int(input("Podaj temperaturę w stopniach Celsjusza: "))
deszcz = input("Czy pada deszcz? tak/nie").strip().lower()

if temperatura < 0:
    print("Jest bardzo zimno, ubierz się ciepło!")
    if deszcz == "tak":
        print("I na dodatek pada deszcz! Uważaj na oblodzenia")
elif 0 <= temperatura <=20:
    if deszcz == "tak":
        print("Nie zapomnij parasola")
    print("Jest chłodno, załóż kurtkę")
elif 21 <= temperatura <=30:
    print("Jest ciepło, możesz wyjść w lekkich ubraniach")
    if deszcz == "tak":
        print("Trochę pada, ale to ciepły deszcz")
else:
    print("Jest gorąco!")
    if deszcz == "tak":
        print("Nawet w deszczu jest gorąco")

if deszcz == "nie":
    print("Nie pada deszcz. Jest sucho")



